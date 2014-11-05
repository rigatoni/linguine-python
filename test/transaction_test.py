import unittest
import sys
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
sys.path.append('../src')
sys.path.append('../src/ops')

from transaction import transaction

class transaction_test(unittest.TestCase):

	def setUp(self):
		self.trans = transaction()
		self.test_data = {}
	
	def test_parse_json(self):
		#set up test data
		self.trans = transaction()
		node_env = os.environ['NODE_ENV']
		db = 'linguine-' + node_env
		corpora = MongoClient()[db].corpus
		test_contents_id = corpora.insert({"contents" : "it was the best of times it was the worst of times it was the age of whatever it was the age of whatever"})
		self.test_data = '{"transactionID":"1", "operation":"no_op", "library":"no_library", "data":["' + str(test_contents_id) + '"]}'
		
		#execute code
		self.assertTrue(self.trans.parse_json(self.test_data))

		#clean up
		corpora.remove(test_contents_id)

	def test_run(self):
		#set up test data
		self.trans = transaction()
		self.trans = transaction()
		node_env = os.environ['NODE_ENV']
		db = 'linguine-' + node_env
		corpora = MongoClient()[db].corpus
		test_contents_id = corpora.insert({"contents" : "it was the best of times it was the worst of times it was the age of whatever it was the age of whatever"})
		self.test_data = '{"transactionID":"1", "operation":"no_op", "library":"no_library", "data":["' + str(test_contents_id) + '"]}'

		#execute code
		self.trans.parse_json(self.test_data)
		self.assertEqual(self.trans.run(), "it was the best of times it was the worst of times it was the age of whatever it was the age of whatever")
		
		#clean up
		corpora.remove(test_contents_id)

		print(self.trans.get_json_response())

if __name__ == '__main__':
	unittest.main()