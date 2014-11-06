import unittest
import sys
sys.path.append('../src')
sys.path.append('../src/ops')

from pos_tag import pos_tag

class remove_punct_test(unittest.TestCase):

    def setUp(self):
        self.op = pos_tag()

    def test_run(self):
        self.op = pos_tag()
        self.test_data = 'the old man the boat. john ate an old sandwich, unfortunately.'
        self.assertEqual(self.op.run(self.test_data), 
        [('the', 'DT'), ('old', 'JJ'), ('man', 'NN'), ('the', 'DT'), \
         ('boat', 'NN'), ('john', 'NN'), ('ate', 'VBD'), ('an', 'DT'),\
         ('old', 'JJ'), ('sandwich', 'NN'), ('unfortunately', 'RB')]
)

if __name__ == '__main__':
    unittest.main()
