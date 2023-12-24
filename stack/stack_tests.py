import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# It does not matter which import is commented in or out for your submission
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_1(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    def test_2(self):
        stack = Stack(10)
        self.assertTrue(stack.is_empty())
        stack.push(5)
        self.assertFalse(stack.is_empty())
    def test_3(self):
        stack = Stack(5)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.push(6)
        stack.push(9)
        self.assertEqual(stack.peek(), 9)
        self.assertFalse(stack.is_full())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 9)
    def test_4(self):
        stack = Stack(5)
        self.assertEqual(stack.size(), 0)
        stack.push(10)
        self.assertEqual(stack.size(), 1)
        stack.push(20)
        self.assertEqual(stack.size(), 2)
    def test_5(self):
        stack = Stack(2)
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        with self.assertRaises(IndexError):
            stack.pop()
    def test_6(self):
        stack = Stack(10)
        with self.assertRaises(IndexError):
            for i in range(11):
                stack.push(i)
    def test_7(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.pop()
    def test_8(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.peek()

if __name__ == '__main__': 
    unittest.main()
