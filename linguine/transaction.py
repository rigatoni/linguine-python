import json
import linguine.operation_builder
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId
from linguine.transaction_exception import TransactionException

class Transaction:

    def __init__(self, env=None):
        self.transaction_id = -1
        self.library = None
        self.operation = None
        self.corpora_ids = []
        self.corpora = []
        self.results = None
        self.error = None
        if env:
            self.db = 'linguine-' + env
        elif 'NODE_ENV' in os.environ:
            #Look for Node environment to determine db name.
            self.db = 'linguine-' + os.environ['NODE_ENV']
        else:
            #NODE_ENV not found, default to development
            self.db = 'linguine-development'

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
        except TypeError:
            raise TransactionException('Improperly formatted request.')
        try:
            #connects to MongoDB on localhost:27017
            corpora = MongoClient()[self.db].corpus
            for id in self.corpora_ids:
                self.corpora.append(corpora.find_one({"_id" : ObjectId(str(id))}))
        except (TypeError, InvalidId):
            raise TransactionException('Could not find corpus.')

    def run(self):
        if self.operation == None:
            raise TransactionException('No operation indicated.')
        try:
            op_handler = linguine.operation_builder.get_operation_handler(self.operation)
            self.results = op_handler.run(self)
            return self.results
        except RuntimeError:
            raise TransactionException('Invalid operation requested.')

    def get_json_response(self):
        analysis_collection = MongoClient()[self.db].analysis
        analysis_doc = {'corpora_ids':self.corpora_ids,
                        'cleanup_ids':[],
                        'result':self.results}
        resultID = analysis_collection.insert(analysis_doc)
        response = {'transaction_id': self.transaction_id,
                    'library':self.library,
                    'operation':self.operation,
                    'results':str(resultID)}
        if not self.error == None:
            response['error'] = self.error
        return json.JSONEncoder().encode(response)
