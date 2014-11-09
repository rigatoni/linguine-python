import unittest
from linguine.ops.tfidf import tfidf
from linguine.corpus import Corpus
class tfidf_test(unittest.TestCase):

    def setUp(self):
        self.op = tfidf()

    def test_run(self):
        self.op = tfidf()
        self.test_data = [ Corpus("0","hello", "hello world"), Corpus("1", "goodbye", "goodbye world") ]
        # self.assertEqual(self.op.run(self.test_data), [[(0.4054651081081644, 'hello'),\
        #       (0.0, 'world')], [(0.4054651081081644, 'goodbye'), (0.0, 'world')] ])
        desired_results = []
        desired_results.append({ "term" : "hello", "importance" : 0.4054651081081644, "corpus_id": "0"})
        desired_results.append({ "term" : "world", "importance" : 0.0, "corpus_id" : "0"})
        desired_results.append({ "term" : "goodbye", "importance" : 0.4054651081081644, "corpus_id": "1"})
        desired_results.append({ "term" : "world", "importance" : 0.0, "corpus_id" : "1"})
        results = self.op.run(self.test_data)
        for result in results:
            self.assertTrue(result in desired_results)

if __name__ == '__main__':
    unittest.main()
