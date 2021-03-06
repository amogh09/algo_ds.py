import unittest
from algo_ds.doubly_linked_node import DNode

class TestDNode(unittest.TestCase):
    def test_insert_before(self):
        node = DNode(1)
        node2 = DNode(2)
        node.insert_before(node2)
        self.assertEqual(node.prev, node2)
        self.assertEqual(node2.next, node)

        node3 = DNode(3)
        node.insert_before(node3)
        self.assertEqual(node.prev, node3)
        self.assertEqual(node3.next, node)
        self.assertEqual(node3.prev, node2)
        self.assertEqual(node2.next, node3)

    def test_insert_after(self):
        node = DNode(1)
        node2 = DNode(2)
        node.insert_after(node2)
        self.assertEqual(node.next, node2)
        self.assertEqual(node2.prev, node)

        node3 = DNode(3)
        node.insert_after(node3)
        self.assertEqual(node.next, node3)
        self.assertEqual(node3.prev, node)
        self.assertEqual(node3.next, node2)
        self.assertEqual(node2.prev, node3)

    def test_remove_from_list(self):
        node = DNode(1)
        node2 = DNode(2)
        node.insert_after(node2)
        node.remove_from_list()
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)
        self.assertEqual(node2.next, None)
        self.assertEqual(node2.prev, None)

        node = DNode(1)
        node2 = DNode(2)
        node.insert_before(node2)
        node.remove_from_list()
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)
        self.assertEqual(node2.next, None)
        self.assertEqual(node2.prev, None)

        node = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        node.insert_after(node2)
        node2.insert_after(node3)
        node.remove_from_list()
        self.assertEqual(node.next, None)
        self.assertEqual(node.prev, None)
        self.assertEqual(node2.next, node3)
        self.assertEqual(node2.prev, None)
        self.assertEqual(node3.next, None)
        self.assertEqual(node3.prev, node2)

        node = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        node.insert_after(node2)
        node2.insert_after(node3)
        node3.remove_from_list()
        self.assertEqual(node3.next, None)
        self.assertEqual(node3.prev, None)
        self.assertEqual(node.next, node2)
        self.assertEqual(node2.prev, node)
        self.assertEqual(node.prev, None)
        self.assertEqual(node2.next, None)

        node = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        node.insert_after(node2)
        node2.insert_after(node3)
        node2.remove_from_list()
        self.assertEqual(node2.next, None)
        self.assertEqual(node2.prev, None)
        self.assertEqual(node.next, node3)
        self.assertEqual(node3.prev, node)

    def test_is_reachable(self):
        node = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        self.assertEqual(node.is_reachable(node2), False)
        node.insert_after(node2)
        self.assertEqual(node.is_reachable(node2), True)
        node2.insert_after(node3)
        self.assertEqual(node.is_reachable(node3), True)
        self.assertEqual(node2.is_reachable(node3), True)

    def test_swap_data(self):
        node = DNode(1)
        node2 = DNode(2)
        DNode.swap_data(node, node2)
        self.assertEqual(node.val, 2)
        self.assertEqual(node2.val, 1)

if __name__ == '__main__':
    unittest.main()
