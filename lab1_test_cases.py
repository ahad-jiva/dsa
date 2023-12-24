import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter1(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter2(self):
        tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_list_iter(tlist), 9)

    def test_max_list_iter3(self):
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec1(self):
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([1,2,3,4,5,6,7,8,9]), [9,8,7,6,5,4,3,2,1])

    def test_reverse_rec3(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_reverse_rec4(self):
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search1(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(7, 0, len(list_val) - 1, list_val), 5)

    def test_bin_search2(self):
        list_val = [0]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)

    def test_bin_search3(self):
        list_val = [1,2,3,4,5,6,7,8,9]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), None)

    def test_bin_search4(self):
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(0, 0, 0, list_val)

    def test_bin_search5(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)

    def test_reverse_list_mutate1(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(tlist)

    def test_reverse_list_mutate2(self):
        tlist = [1,2,3,4,5,6,7,8,9]
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [9,8,7,6,5,4,3,2,1])

    def test_reverse_list_mutate3(self):
        tlist = []
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [])

    def test_reverse_list_mutate4(self):
        tlist = [1]
        reverse_list_mutate(tlist)
        self.assertEqual(tlist, [1])


if __name__ == "__main__":
    unittest.main()
