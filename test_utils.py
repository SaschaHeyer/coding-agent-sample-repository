import unittest
from utils import find_maximum

class TestFindMaximum(unittest.TestCase):
    def test_find_maximum(self):
        self.assertEqual(find_maximum([3, 1, 4, 1, 5, 9, 2, 6]), 9)  # Expected: 9, but bug returns 6

if __name__ == "__main__":
    unittest.main()
