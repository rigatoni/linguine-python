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
        self.corpora_ids = []
        self.corpora = []

    def parse_json(self, json_data):
        try:
            input_data = json.loads(json_data)
            self.transaction_id = input_data['transaction_id']
            self.operation = input_data['operation']
            self.library = input_data['library']
            self.corpora_ids = input_data['corpora_ids']
        except KeyError:
            raise TransactionException('Missing property transaction_id, operation, library, or corpora_ids.')
        except ValueError:
            raise TransactionException('Could not parse JSON.')
        try:
            #load corpora from database
            corpora = DatabaseAdapter.getDB().corpus
            for id in self.corpora_ids:
                corpus = corpora.find_one({"_id" : ObjectId(id)})
                self.corpora.append(Corpus(id, corpus["contents"], corpus["title"], corpus["tags"]))
        except (TypeError, InvalidId):
            raise TransactionException('Could not find corpus.')

    def run(self):
        op_handler = linguine.operation_builder.get_operation_handler(self.operation)
        analysis = {'corpora_ids':self.corpora_ids,
                    'cleanup_ids':[],
                    'result':op_handler.run(self.corpora),
                    'analysis':self.operation}
        analysis_id = DatabaseAdapter.getDB().analyses.insert(analysis)
        response = {'transaction_id': self.transaction_id,
                    'library':self.library,
                    'operation':self.operation,
                    'results':str(analysis_id)}
        return json.JSONEncoder().encode(response)
