import unittest
from algo_ds.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        self.assertEqual(ll.head.val, 3)
        self.assertEqual(ll.head.next.val, 2)
        self.assertEqual(ll.head.next.next.val, 1)

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end(1)
        ll.insert_at_end(2)
        ll.insert_at_end(3)
        self.assertEqual(ll.head.val, 1)
        self.assertEqual(ll.head.next.val, 2)
        self.assertEqual(ll.head.next.next.val, 3)

    def test_remove(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        self.assertEqual(ll.remove(), 50)
        self.assertEqual(ll.remove(), 80)
        self.assertEqual(ll.remove(), 40)
        self.assertEqual(ll.as_python_list(), [60, 10, 30])
        self.assertEqual(ll.remove(), 60)
        self.assertEqual(ll.remove(), 10)
        self.assertEqual(ll.remove(), 30)
        self.assertRaises(IndexError, ll.remove)

    def test_remove_from_end(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        self.assertEqual(ll.remove_from_end(), 30)
        self.assertEqual(ll.remove_from_end(), 10)
        self.assertEqual(ll.remove_from_end(), 60)
        self.assertEqual(ll.as_python_list(), [50, 80, 40])
        self.assertEqual(ll.remove_from_end(), 40)
        self.assertEqual(ll.remove_from_end(), 80)
        self.assertEqual(ll.remove_from_end(), 50)
        self.assertRaises(IndexError, ll.remove_from_end)

    def test_length(self):
        ll = self.get_test_list()
        self.assertEqual(ll.length(), 6)
        ll.remove()
        self.assertEqual(ll.length(), 5)

    def test_swap(self):
        ll = self.get_test_list()
        ll.swap(80, 10)
        self.assertEqual(ll.as_python_list(), [50, 10, 40, 60, 80, 30])
        ll.swap(40, 60)
        self.assertEqual(ll.as_python_list(), [50, 10, 60, 40, 80, 30])
        ll.swap(50, 10)
        self.assertEqual(ll.as_python_list(), [10, 50, 60, 40, 80, 30])

    def test_reverse(self):
        ll = self.get_test_list()
        self.assertEqual(ll.as_python_list(), [50, 80, 40, 60, 10, 30])
        ll.reverse()
        self.assertEqual(ll.as_python_list(), [30, 10, 60, 40, 80, 50])

        ll = LinkedList()
        ll.insert(100)
        ll.reverse()
        self.assertEqual(ll.as_python_list(), [100])

    def test_reverse_groups(self):
        ll = self.get_test_list()
        ll.reverse_groups(3)
        self.assertEqual(ll.as_python_list(), [40, 80, 50, 30, 10, 60])
        ll.reverse_groups(4)
        self.assertEqual(ll.as_python_list(), [30, 50, 80, 40, 10, 60])
        ll.reverse_groups(6)
        self.assertEqual(ll.as_python_list(), [60, 10, 40, 80, 50, 30])
        ll.reverse_groups(1)
        self.assertEqual(ll.as_python_list(), [60, 10, 40, 80, 50, 30])

    def test_merge_sort(self):
        ll = self.get_test_list()
        ll.merge_sort()
        self.assertEqual(ll.as_python_list(), [10, 30, 40, 50, 60, 80])

    def get_test_list(self):
        ll = LinkedList()
        ll.insert(30)
        ll.insert(10)
        ll.insert(60)
        ll.insert(40)
        ll.insert(80)
        ll.insert(50)
        return ll

    def get_test_list2(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(50)
        ll.insert(20)
        ll.insert(70)
        ll.insert(65)
        ll.insert(25)
        return ll

if __name__ == '__main__':
    unittest.main()
