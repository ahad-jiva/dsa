import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 10])
        self.assertTrue(t_list.remove(10))
        self.assertFalse(t_list.remove(999))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_adding(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        t_list.add(1)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.add(1))
        self.assertEqual(t_list.python_list(), [1])
        t_list.add(5)
        self.assertEqual(t_list.index(5), 1)
        self.assertEqual(t_list.index(5000), None)

    def test_invalid_pop(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        with self.assertRaises(IndexError):
            t_list.pop(800)
        with self.assertRaises(IndexError):
            t_list.pop(-2)

    def test_index(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(10)
        t_list.add(965)
        t_list.add(300)
        self.assertEqual(t_list.index(300), 4)
        self.assertEqual(t_list.index(964), None)

    def test_pop(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(10)
        t_list.add(965)
        t_list.add(300)
        self.assertEqual(t_list.pop(4), 300)
        self.assertEqual(t_list.pop(4), 965)
        self.assertEqual(t_list.pop(3), 10)
        with self.assertRaises(IndexError):
            t_list.pop(800)

    def test_search(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(10)
        t_list.add(965)
        t_list.add(300)
        self.assertTrue(t_list.search(5))
        self.assertTrue(t_list.search(300))
        self.assertFalse(t_list.search(500))

    def test_list(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(10)
        t_list.add(965)
        t_list.add(300)
        self.assertEqual(t_list.python_list(), [1, 3, 5, 10, 300, 965])
        t_list.add(587)
        self.assertEqual(t_list.python_list(), [1, 3, 5, 10, 300, 587, 965])
        t_list.remove(1)
        self.assertEqual(t_list.python_list(), [3, 5, 10, 300, 587, 965])

    def test_list_reversed(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(1)
        t_list.add(5)
        t_list.add(3)
        t_list.add(10)
        t_list.add(965)
        t_list.add(300)
        self.assertEqual(t_list.python_list_reversed(), [965, 300, 10, 5, 3, 1])
        t_list.add(587)
        self.assertEqual(t_list.python_list_reversed(), [965, 587, 300, 10, 5, 3, 1])
        t_list.remove(1)
        self.assertEqual(t_list.python_list_reversed(), [965, 587, 300, 10, 5, 3])

    def test_size(self):
        t_list = OrderedList()
        self.assertEqual(t_list.size(), 0)
        t_list.add(1)
        self.assertEqual(t_list.size(), 1)
        t_list.add(5)
        self.assertEqual(t_list.size(), 2)
        t_list.add(3)
        self.assertEqual(t_list.size(), 3)
        t_list.add(10)
        self.assertEqual(t_list.size(), 4)
        t_list.add(965)
        self.assertEqual(t_list.size(), 5)
        t_list.add(300)
        self.assertEqual(t_list.size(), 6)
        t_list.remove(300)
        t_list.remove(965)
        self.assertEqual(t_list.size(), 4)
        t_list.pop(0)
        self.assertEqual(t_list.size(), 3)


if __name__ == '__main__':
    unittest.main()
