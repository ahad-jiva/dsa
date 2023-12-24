import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    # Trivial Test
    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_isempty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(1, "1")
        self.assertFalse(bst.is_empty())
        bst.insert(2, "5")
        self.assertFalse(bst.is_empty())

    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        self.assertTrue(bst.search(1))
        self.assertTrue(bst.search(2))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(4))
        self.assertFalse(bst.search(5))
        self.assertFalse(bst.search(-1))

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(4, "4")
        self.assertEqual(bst.inorder_list(), [1, 4])
        bst.insert(5, "5")
        self.assertEqual(bst.inorder_list(), [1, 4, 5])
        bst.insert(2, "2")
        self.assertEqual(bst.inorder_list(), [1, 2, 4, 5])
        bst.insert(3, "3")
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5])

    def test_find_min1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.find_min(), (1, "1"))

    def test_find_min2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.find_min(), (1, "1"))

    def test_find_min_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_min(), None)

    def test_find_max1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        self.assertEqual(bst.find_max(), (4, "4"))
        bst.insert(5, "5")
        self.assertEqual(bst.find_max(), (5, "5"))

    def test_find_max2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        self.assertEqual(bst.find_max(), (4, "4"))
        bst.insert(5, "5")
        self.assertEqual(bst.find_max(), (5, "5"))

    def test_find_max_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.find_max(), None)

    def test_tree_height1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.tree_height(), 4)

    def test_tree_height2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.tree_height(), 2)

    def test_tree_height_empty(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)

    def test_inorder1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5])
        bst.insert(6, "6")
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5, 6])

    def test_inorder2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        bst.insert(6, "6")
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 6])
        bst.insert(5, "5")
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5, 6])

    def test_preorder1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.preorder_list(), [1, 2, 3, 4, 5])
        bst.insert(6, "6")
        self.assertEqual(bst.preorder_list(), [1, 2, 3, 4, 5, 6])

    def test_preorder2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.preorder_list(), [3, 2, 1, 4, 5])
        bst.insert(6, "6")
        self.assertEqual(bst.preorder_list(), [3, 2, 1, 4, 5, 6])

    def test_levelorder1(self):
        bst = BinarySearchTree()
        bst.insert(1, "1")
        bst.insert(2, "2")
        bst.insert(3, "3")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.level_order_list(), [1, 2, 3, 4, 5])
        bst.insert(6, "6")
        self.assertEqual(bst.level_order_list(), [1, 2, 3, 4, 5, 6])

    def test_levelorder2(self):
        bst = BinarySearchTree()
        bst.insert(3, "3")
        bst.insert(2, "2")
        bst.insert(1, "1")
        bst.insert(4, "4")
        bst.insert(5, "5")
        self.assertEqual(bst.level_order_list(), [3, 2, 4, 1, 5])
        bst.insert(6, "6")
        self.assertEqual(bst.level_order_list(), [3, 2, 4, 1, 5, 6])


if __name__ == '__main__': 
    unittest.main()
