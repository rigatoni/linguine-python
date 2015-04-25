import unittest
import sys

from linguine.ops.sentence_tokenize import SentenceTokenize

class SentenceTokenizeTest(unittest.TestCase):

    def setUp(self):
        self.op = SentenceTokenize()

    def test_run(self):
        self.op = SentenceTokenize()
        self.test_data = [ Corpus("0","hello", "hello world. Will you say goodbye, world? I'll say hello.")]
        self.assertEqual(self.op.run(self.test_data),
            {'corpus_id':'0', 'sentences': ["hello world.", "Will you say goodbye, world?","I'll say hello."}
if __name__ == '__main__':
    unittest.main()
