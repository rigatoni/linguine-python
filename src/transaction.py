import json
import operation_builder
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

class Transaction:

    def __init__(self):
        self.transactionID = -1
        self.library = None
        self.operation = None
        self.data_ids = []
        self.data = []
        self.results = None
        self.error = None
        self.db = None

    def parse_json(self, json_data):
        try:
            input_data = json.loads(json_data)
            self.transactionID = input_data['transactionID']
            self.operation = input_data['operation']
            self.library = input_data['library']
            self.data_ids = input_data['data']
            #self.results = input_data['results']
        except TypeError:
            self.error = "Improperly formatted request"
            return False

        try:
            #Look for Node environment to determine db name.
            self.db = 'linguine-' + os.environ['NODE_ENV']
        except KeyError:
            #NODE_ENV not found, default to development
            self.db = 'linguine-development'

        try:
            #connects to MongoDB on localhost:27017
            corpora = MongoClient()[self.db].corpus
            for dataID in self.data_ids:
                self.data.append(corpora.find_one({"_id" : ObjectId(dataID)})['contents'])
            return True
        except TypeError:
            self.error = "Could not find requested data ID"
            return False

    def run(self):
        if self.operation == None:
            self.error = "No operation indicated"
            return False
        try:
            op_handler = operation_builder.get_operation_handler(self.operation)
            self.results = op_handler.run(self.data)
            return self.results
        except RuntimeError:
            self.error = "Invalid operation requested"
            return False

    def get_json_response(self):
        analysis_collection = MongoClient()[self.db].analysis
        analysis_doc = {'corpora_ids':self.data_ids, 'cleanup_ids':[], 'result':self.results}
        resultID = analysis_collection.insert(analysis_doc)
        response = {'transactionID':self.transactionID, 'library':self.library, 'operation':self.operation, 'results':str(resultID)}
        if not self.error == None:
            response['error'] = self.error
        return json.JSONEncoder().encode(response)
