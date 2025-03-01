import unittest
from utils import find_maximum, find_minimum

class TestFindMaximum(unittest.TestCase):
    def test_find_maximum(self):
        self.assertEqual(find_maximum([3, 1, 4, 1, 5, 9, 2, 6]), 9)

class TestFindMinimum(unittest.TestCase):
    def test_find_minimum(self):
        self.assertEqual(find_minimum([3, 1, 4, 1, 5, 9, 2, 6]), 1)