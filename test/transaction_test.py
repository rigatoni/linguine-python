import unittest
import sys
sys.path.append('../src')
sys.path.append('../src/ops')

from transaction import transaction

class transaction_test(unittest.TestCase):

	def setUp(self):
		self.trans = transaction()
		self.test_data = {}
	
	def test_parse_json(self):
		self.trans = transaction()
		self.test_data = '{"transactionID":"1", "operation":"no_op", "library":"no_library", "data":"000"}'
		self.assertTrue(self.trans.parse_json(self.test_data))

	def test_run(self):
		self.trans = transaction()
		self.test_data = '{"transactionID":"1", "operation":"no_op", "library":"no_library", "data":"000"}'
		self.trans.parse_json(self.test_data)

		self.assertEqual(self.trans.run(), "The quick brown fox jumps over the lazy dog.")

if __name__ == '__main__':
	unittest.main()