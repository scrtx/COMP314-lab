import unittest
from search import linear_search, binary_search

class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values = [13, 23, 7, 5, 2, 11, 19, 31]
        res = linear_search(values, 31)
        self.assertEqual(res, 7)
        self.assertEqual(linear_search(values, 11), 5)
        self.assertEqual(linear_search(values, 13), 0)

    def test_binary_search(self):
        values = [13, 23, 7, 5, 2, 11, 19, 31]
        values.sort()
        res = binary_search(values, 31, 0, len(values) - 1)
        self.assertEqual(res, 7)
        self.assertEqual(binary_search(values, 5, 0, len(values) - 1), 1)
        self.assertEqual(binary_search(values, 2, 0, len(values) - 1), 0)
    
if __name__ == "__main__":
    unittest.main()