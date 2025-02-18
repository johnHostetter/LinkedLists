"""
A script to test the functionality of the Node class.
"""

import unittest

from node import DoubleLinkNode


class TestNode(unittest.TestCase):
    """
    A TestCase class to help ensure the Node class is functional as expected.
    """

    def test_create_node(self) -> None:
        """
        Test the creation of a Node object.

        Returns:
            None
        """
        node = DoubleLinkNode(5)
        self.assertEqual(5, node)  # first arg is expected, second is actual
        self.assertIsNone(node.prev)  # node has no predecessor
        self.assertIsNone(node.next)  # node has no successor
        self.assertEqual("5", str(node))  # first arg is expected, second is actual
        self.assertEqual("5", repr(node))  # first arg is expected, second is actual
        self.assertEqual(hash(5), hash(node))  # first arg is expected, second is actual

    def test_node_equality(self) -> None:
        """
        Test the equality of Node objects.

        Returns:
            None
        """
        node1 = DoubleLinkNode(5)
        self.assertEqual(
            node1, DoubleLinkNode(5)
        )  # equal to another node with the same data
        self.assertNotEqual(
            node1, DoubleLinkNode(6)
        )  # not equal to another node with different data
        self.assertNotEqual(node1, None)  # not equal to None


if __name__ == "__main__":
    unittest.main()
