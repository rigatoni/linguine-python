import unittest
import sys

from linguine.ops.pos_tag import PosTag

class PosTagTest(unittest.TestCase):

    def setUp(self):
        self.op = PosTag()

    def test_run(self):
        self.op = PosTag()
        self.test_data = 'the old man the boat. john ate an old sandwich, unfortunately.'
        self.assertEqual(self.op.run(self.test_data),
        [('the', 'DT'), ('old', 'JJ'), ('man', 'NN'), ('the', 'DT'), \
         ('boat', 'NN'), ('john', 'NN'), ('ate', 'VBD'), ('an', 'DT'),\
         ('old', 'JJ'), ('sandwich', 'NN'), ('unfortunately', 'RB')]
)

if __name__ == '__main__':
    unittest.main()
