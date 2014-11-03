import json
import operation_builder
from pymongo import MongoClient
from bson.objectid import ObjectId

class transaction:

	def __init__(self):
		self.transactionID = -1
		self.library = None
		self.operation = None
		self.data = None
		self.results = None
		self.error = None

	def parse_json(self, json_data):
		try:
			input_data = json.loads(json_data)
			self.transactionID = input_data['transactionID']
			self.operation = input_data['operation']
			self.library = input_data['library']
			dataID = input_data['data']
		except TypeError:
			self.error = "Improperly formatted request"
			return False

		try:
			corpora = MongoClient().linguine.corpora
			self.data = corpora.find_one({"_id" : ObjectId(dataID)})['text']
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
		resultsCollection = MongoClient().linguine.results
		resultID = resultsCollection.insert(self.results)
		response = {'transactionID':self.transactionID, 'library':self.library, 'operation':self.operation, 'results':str(resultID)}
		if not self.error == None:
			response['error'] = self.error
		return json.JSONEncoder().encode(response)
