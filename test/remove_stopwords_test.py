import unittest
import sys

from linguine.ops.remove_stopwords import RemoveStopwords

class RemoveStopwordsTest(unittest.TestCase):

    def setUp(self):
        self.op = RemoveStopwords()

    def test_run(self):
        self.op = RemoveStopwords()
        self.test_data = []
        self.assertEqual(self.op.run(self.test_data),
        ['quick,','brown','fox','jumps','over','lazy','dogs']
)

if __name__ == '__main__':
    unittest.main()
