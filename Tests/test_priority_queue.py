import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_enqueue(self):
        self.pq.enqueue('D1', 0)
        self.assertEqual(len(self.pq.heap), 1)
        self.assertEqual(self.pq.heap[0][1], 'D1')

        self.pq.enqueue('P1', 1)
        self.assertEqual(len(self.pq.heap), 2)
        self.assertEqual(self.pq.heap[1][1], 'D1')
        
        self.pq.enqueue('E1', 100)
        self.assertEqual(len(self.pq.heap), 3)
        self.assertEqual(self.pq.heap[0][1], 'E1')


    def test_dequeue(self):
        self.pq.enqueue('D1', 0)
        self.pq.enqueue('E1', 100)
        self.pq.enqueue('P2', 1)

        item = self.pq.dequeue()
        self.assertEqual(item[1], 'E1')
        self.assertEqual(len(self.pq.heap), 2)

        item = self.pq.dequeue()
        self.assertEqual(item[1], 'P2')
        self.assertEqual(len(self.pq.heap), 1)
        
        item = self.pq.dequeue()
        self.assertEqual(item[1], 'D1')
        self.assertEqual(len(self.pq.heap), 0)


    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.pq.enqueue('D1', 0)
        self.assertFalse(self.pq.is_empty())
        self.pq.dequeue()
        self.assertTrue(self.pq.is_empty())


if __name__ == '__main__':
    unittest.main()
