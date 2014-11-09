import unittest
import sys

from linguine.ops.remove_punct import RemovePunct

class RemovePunctTest(unittest.TestCase):

    def setUp(self):
        self.op = RemovePunct()

    def test_run(self):
        self.op = RemovePunct()
        self.test_data = '''He said,"that's it." *u* Hello, World. O'Rourke is rockin'.'''
        self.assertEqual(self.op.run(self.test_data), '''He said that s it Hello World O Rourke is rockin''')

if __name__ == '__main__':
    unittest.main()
