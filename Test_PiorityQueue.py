import unittest
from piorityQueue import *

class TestPriorityQueue(unittest.TestCase):
    def test_enqueue(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)

       # print(pq.head.item)
        self.assertEqual(pq.getsize(), 5)
        self.assertEqual(pq.peek(), "item3")

    def test_dequeue(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)


        self.assertEqual(pq.dequeue(), "item3")
        self.assertEqual(pq.getsize(), 4)
        self.assertEqual(pq.peek(), "item2")       

    def test_peek(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)


        self.assertEqual(pq.peek(), "item3")

    def test_change_priority(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)

        pq.changePiority("item1", 4)
        self.assertEqual(pq.peek(), "item1")    

    def test_remove(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)

        pq.remove("item2")
        self.assertEqual(pq.getsize(), 4)
        self.assertEqual(pq.peek(), "item3")  

    def test_clear(self):
        pq = PiorityQueue()
        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)

        pq.clear()
        self.assertTrue(pq.isEmpty())

    def test_is_empty(self):
        pq = PiorityQueue()

        self.assertTrue(pq.isEmpty())

        pq.enqueue("item1", 1)
        pq.enqueue("item2", 2)
        pq.enqueue("item3", 3)
        pq.enqueue("item4", 2)
        pq.enqueue("item5", 1)    

        self.assertFalse(pq.isEmpty())
     

if __name__ == '__main__':
    unittest.main()