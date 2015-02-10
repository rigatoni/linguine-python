import unittest
import sys

from linguine.ops.topic_model import TopicModel

class TopicModelTest(unittest.TestCase):

    def setUp(self):
        self.op = TopicModel()

    def test_run(self):
        self.op = TopicModel()
        self.test_data = [line.strip() for line in open('brown.txt','r')]
        self.test_data = [[w for w in d.lower().split() ] for d in self.test_data]
        print(TopicModel(self.test_data))

if __name__ == '__main__':
    unittest.main()
