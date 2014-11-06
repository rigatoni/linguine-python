import unittest
import sys

from linguine.ops.remove_punct import remove_punct

class remove_punct_test(unittest.TestCase):

    def setUp(self):
        self.op = remove_punct()

    def test_run(self):
        self.op = remove_punct()
        self.test_data = '''He said,"that's it." *u* Hello, World. O'Rourke is rockin'.'''
        self.assertEqual(self.op.run(self.test_data), '''He said that s it Hello World O Rourke is rockin''')

if __name__ == '__main__':
    unittest.main()
