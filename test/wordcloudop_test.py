import unittest
from linguine.ops.word_cloud_op import WordCloudOp
from linguine.corpus import Corpus

class WordCloudOpTest(unittest.TestCase):

    def setUp(self):
        self.op = WordCloudOp()

    def test_run(self):
        self.op = WordCloudOp()
        self.test_data = [ Corpus("0","hello", "hello world hello hello world test") ]
        desired_results = []
        desired_results.append({ "term" : "hello", "frequency" : 3})
        desired_results.append({ "term" : "world", "frequency" : 2})
        desired_results.append({ "term" : "test", "frequency" : 1})
        #results = self.op.run(self.test_data)
        #for result in results:
        #    self.assertTrue(result in desired_results)

if __name__ == '__main__':
    unittest.main()
