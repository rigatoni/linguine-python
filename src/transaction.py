import json
import operation_builder

class transaction:

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

			#for testing purposes until MongoDB is integrated
			self.data = "The quick brown fox jumps over the lazy dog."
			return True
		except TypeError:
			return False

	def run(self):
		if self.operation == None:
			print("no")
			return False
		try:
			op_handler = operation_builder.get_operation_handler(self.operation)
			self.results = op_handler.run(self.data)
			return self.results
		except RuntimeError:
			print("couldn't build")
			return False
		
	def get_json_response(self):
		response = {'transactionID':self.transactionID, 'library':self.library, 'operation':self.operation, 'results':self.results}
		return json.JSONEncoder().encode(response)
