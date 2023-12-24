import unittest

# Use the imports below to test either your array-based queue
# or your link-based version
# It does not matter which import is commented in or out for your final submission

from queue_array import Queue
#from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue_trivial(self):
        '''***Trivial*** test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    def test_queue_enqueue(self):
        q = Queue(5)
        q.enqueue(5)
        self.assertEqual(q.size(), 1)
        q.enqueue(6)
        q.enqueue(7)
        self.assertEqual(q.size(), 3)
    def test_queue_size(self):
        q = Queue(100)
        q.enqueue(4)
        self.assertEqual(q.size(), 1)
        q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)
    def test_queue_dequeue(self):
        q = Queue(20)
        q.enqueue(1)
        q.enqueue(12)
        self.assertEqual(q.dequeue(), 1)
    def test_queue_enqueue_on_full(self):
        q = Queue(4)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        q.enqueue(1)
        with self.assertRaises(IndexError):
            q.enqueue(1)
    def test_queue_dequeue_on_empty(self):
        q = Queue(6)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_queue_enqueue_dequeue_loop(self):
        q = Queue(100)
        for i in range(100):
            q.enqueue(i)
        for i in range(100):
            self.assertEqual(q.dequeue(), i)
    def test_queue_enqueue_loop(self):
        q = Queue(10000)
        for i in range(10000):
            q.enqueue(i)
        self.assertEqual(q.size(), 10000)
        for i in range(5000):
            self.assertEqual(q.dequeue(), i)
        self.assertEqual(q.size(), 5000)


if __name__ == '__main__': 
    unittest.main()
