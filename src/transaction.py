import json
import operation_builder

class Transaction:

	def __init__(self):
		self.transactionID = -1
		self.library = None
		self.operation = None
		self.data = None
		self.results = None

	def parse_json(self, json_data):
		try:
			input_data = json.loads(json_data)
			self.transactionID = input_data['transactionID']
			self.operation = input_data['operation']
			self.library = input_data['library']
			self.data = input_data['data']
		except TypeError:
			return False

	def run(self):
		if self.operation == None:
			return False
		try:
			op_handler = operation_builder.get_operation_handler(self.operation)
			self.results = op_handler.run(self.data)
			return True
		except RuntimeError:
			return False
		
	def get_json_response(self):
		response = {'transactionID':self.transactionID, 'operation':self.operation, 'library':self.library, 'results':self.results}
		return json.JSONEncoder().encode(response)
