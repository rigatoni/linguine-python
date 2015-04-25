import unittest
import sys

from linguine.ops.word_tokenize import WordTokenizeTreebank, WordTokenizeWhitespacePunct, WordTokenizeStanford, WordTokenizeSpaces, WordTokenizeSpaces

class PosTagTest(unittest.TestCase):

    def setUp(self):
        self.op = WordTokenizeTreebank()

    def test_run(self):
        self.op = WordTokenizeSpaces()
        self.test_data = [ Corpus("0","hello", "hello world"), Corpus("1", "goodbye", "goodbye world") ]
        desired_results = []
        desired_results.append({ "corpus_id" : "0", "tokenized_content" : ["hello","world"]})
        desired_results.append({ "corpus_id" : "1", "tokenized_content" : ["goodbye","world"]})
)

if __name__ == '__main__':
    unittest.main()
