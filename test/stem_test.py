import unittest
import sys

from linguine.ops.stem import StemmerLancaster, StemmerPorter, StemmerSnowball

class PosTagTest(unittest.TestCase):

    def setUp(self):
        self.op = StemmerLancaster()

    def test_lancaster(self):
        self.op = StemmerLancaster()
        self.test_data = ['strange','women','lying','ponds','distributing','swords','no','basis','system','government']
        self.assertEqual(self.op.run(self.test_data),
        ['starnge','wom','lying','pond','distribut','sword','no','bas','system','govern']

    def test_porter(self):
        self.op = StemmerPorter()
        self.test_data = ['strange','women','lying','ponds','distributing','swords','no','basis','system','government']
        self.assertEqual(self.op.run(self.test_data),
        ['strang','women','lie','pond','distribut','sword','no','basi','system','govern']

    def test_snowball(self):
        self.op = StemmerSnowball()
        self.test_data = ['strange','women','lying','ponds','distributing','swords','no','basis','system','government']
        self.assertEqual(self.op.run(self.test_data),
        ['strang','women','lie','pond','distribut','sword','no','basi','system','govern']
    def test_run(self):
        self.test_lancaster()
        self.test_porter()
        self.test_snowball()
)

if __name__ == '__main__':
    unittest.main()
