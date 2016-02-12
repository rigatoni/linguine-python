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
        self.time_created = None
        self.corpora = []
        self.analysis_name = ""
        self.cleanups = []
        self.tokenizer = None

        self.token_based_operations = ['tfidf','word_cloud_op','stem_porter','stem_lancaster','stem_snowball','lemmatize_wordnet']
    
    #Read in all corpora that are specified for a given transaction
    def read_corpora(self, corpora_ids):
        try:
            #load corpora from database
            corpora = DatabaseAdapter.getDB().corpus
            for id in self.corpora_ids:
                corpus = corpora.find_one({"_id" : ObjectId(id)})
                self.corpora.append(Corpus(id, corpus["title"], corpus["contents"], corpus["tags"]))
        except (TypeError, InvalidId):
            raise TransactionException('Could not find corpus.')
    
    #Insert an analysis record into the database,
    # acknowledging that an analysis is to be processed.
    def create_analysis_record(self):
        analysis = {'user_id':ObjectId(self.user_id),
                    'analysis_name': self.analysis_name,
                    'corpora_ids':self.corpora_ids,
                    'cleanup_ids':self.cleanups,
                    'result': "",
                    'complete': False,
                    'time_created': self.time_created,
                    'analysis':self.operation}

        return DatabaseAdapter.getDB().analyses.insert(analysis)
    
    #Parse a JSON request from the linguine-node webserver,
    #Requesting that an analysis should be preformed
    def parse_json(self, json_data):
        try:
            input_data = json.loads(json_data.decode())

            self.transaction_id = input_data['transaction_id']
            self.operation = input_data['operation']
            self.library = input_data['library']
            self.analysis_name = input_data['analysis_name']
            self.time_created = input_data['time_created']
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

    def run(self):
        corpora = self.corpora
        tokenized_corpora = []
        analysis = {}
        
        if not self.tokenizer == None and not self.tokenizer == '':
            op_handler = linguine.operation_builder \
            .get_operation_handler(self.tokenizer)
            tokenized_corpora = op_handler.run(corpora)
        
        for cleanup in self.cleanups:

            op_handler = linguine.operation_builder.\
            get_operation_handler(cleanup)
            corpora = op_handler.run(corpora)
            
            #Corpora must be re tokenized after each cleanup
            if not self.tokenizer == None and not self.tokenizer == '':
              op_handler = linguine.operation_builder \
              .get_operation_handler(self.tokenizer)
              tokenized_corpora = op_handler.run(corpora)

        op_handler = linguine.operation_builder.get_operation_handler(self.operation)
        return op_handler.run(corpora)

