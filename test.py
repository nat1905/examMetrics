import unittest
from main import isfinite


class isfiniteTest(unittest.TestCase):


    def test_positive(self):

        res = isfinite(6)
        self.assertEqual(True, res)

    def test_zero(self):

        res = isfinite(0)
        self.assertEqual(True, res)

    def test_negative(self):

        self.assertRaises(ValueError, isfinite, "jjj")


if __name__ == "__main__":
    unittest.main()