import unittest

from Percept.Perceptrons import *


class MyTestCase(unittest.TestCase):

    def test_length(self):
        self.assertRaises(AssertionError, pAND.feed([1.0, 1.0, 1.0]))

    def test_pAND(self):
        self.assertEqual(pAND.feed([0, 0]), False)
        self.assertEqual(pAND.feed([1.0, 1.0]), True)
        self.assertEqual(pAND.feed([1.0, 0]), False)
        self.assertEqual(pAND.feed([0, 1.0]), False)

    def test_pOR(self):
        self.assertEqual(pOR.feed([0, 0]), False)
        self.assertEqual(pOR.feed([1.0, 1.0]), True)
        self.assertEqual(pOR.feed([1.0, 0]), True)
        self.assertEqual(pOR.feed([0, 1.0]), True)

    def test_pNAND(self):
        self.assertEqual(pNAND.feed([0, 0]), True)
        self.assertEqual(pNAND.feed([1.0, 1.0]), False)
        self.assertEqual(pNAND.feed([1.0, 0]), True)
        self.assertEqual(pNAND.feed([0, 1.0]), True)

    def test_SUM(self):
        self.assertEqual(pSum.__init__(0,0).feed(), (False, False))
        self.assertEqual(pSum.__init__(0,1.0).feed(), (True, False))
        self.assertEqual(pSum.__init__(1.0,0).feed(), (True, False))
        self.assertEqual(pSum.__init__(1.0,1.0).feed(),(False, True))



if __name__ == '__main__':
    unittest.main()
