import json
import linguine.operation_builder
from linguine.corpus import Corpus
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from linguine.database_adapter import DatabaseAdapter
from linguine.transaction_exception import TransactionException

class Transaction:
    
    def __init__(self, env=None):
        self.transaction_id = -1
        self.library = None
        self.operation = None
        self.user_id = None
        self.corpora_ids = []
        self.corpora = []
        self.cleanups = []
        self.tokenizer = []
        #TOKENIZER LIST: If a new operation requires a user-selected tokenizer, add it here
        self.token_based_operations = ['tfidf','word_cloud_op','stem_porter','stem_lancaster','stem_snowball','lemmatize_wordnet']

    def parse_json(self, json_data):
        try:
            input_data = json.loads(json_data.decode())
            print(input_data)
            self.transaction_id = input_data['transaction_id']
            self.operation = input_data['operation']
            self.library = input_data['library']
            if 'user_id' in input_data.keys():
                self.user_id = input_data['user_id']
            if 'cleanup' in input_data.keys():
                self.cleanups = input_data['cleanup']
            self.corpora_ids = input_data['corpora_ids']
            if 'tokenizer' in input_data.keys():
                self.tokenizer = input_data['tokenizer']
        except KeyError:
            raise TransactionException('Missing property transaction_id, operation, library, tokenizer or corpora_ids.')
        except ValueError:
            raise TransactionException('Could not parse JSON.')
        try:
            #load corpora from database
            corpora = DatabaseAdapter.getDB().corpus
            for id in self.corpora_ids:
                corpus = corpora.find_one({"_id" : ObjectId(id)})
                self.corpora.append(Corpus(id, corpus["title"], corpus["contents"], corpus["tags"]))
        except (TypeError, InvalidId):
            raise TransactionException('Could not find corpus.')

    def run(self):
        corpora = self.corpora
        tokenized_corpora = self.tokenized_corpora
        for cleanup in self.cleanups:
            op_handler = linguine.operation_builder.get_operation_handler(cleanup)
            corpora = op_handler.run(corpora)
        for tokenizer in self.tokenizer:
            op_handler = linguine.operation_builder.get_operation_handler(tokenizer)
            tokenized_corpora = op_handler.run(corpora)
        op_handler = linguine.operation_builder.get_operation_handler(self.operation)
        if self.operation in self.token_based_operations:
            analysis = {'user_id':ObjectId(self.user_id),
                        'corpora_ids':self.corpora_ids,
                        'cleanup_ids':self.cleanups,
                        'result':op_handler.run(tokenized_corpora),
                        'analysis':self.operation}
        else:
            analysis = {'user_id':ObjectId(self.user_id),
                        'corpora_ids':self.corpora_ids,
                        'cleanup_ids':self.cleanups,
                        'result':op_handler.run(corpora),
                        'analysis':self.operation}
        analysis_id = DatabaseAdapter.getDB().analyses.insert(analysis)
        response = {'transaction_id': self.transaction_id,
                    'cleanup_ids': self.cleanups,
                    'library':self.library,
                    'operation':self.operation,
                    'results':str(analysis_id)}
        return json.JSONEncoder().encode(response)
