import unittest
import sys

from linguine.ops.tfidf import tfidf

class tfidf_test(unittest.TestCase):

    def setUp(self):
        self.op = tfidf()

    def test_run(self):
        self.op = tfidf()
        self.test_data = [['hello', 'world'],['goodbye', 'world'] ]
        self.assertEqual(self.op.run(self.test_data), [[(0.4054651081081644, 'hello'),\
              (0.0, 'world')], [(0.4054651081081644, 'goodbye'), (0.0, 'world')] ])

if __name__ == '__main__':
    unittest.main()
