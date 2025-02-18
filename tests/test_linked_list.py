"""
A module to test the SingleLinkedList class.
"""

import unittest
from typing import Tuple

from node import Node, SingleLinkNode, DoubleLinkNode
from linked_list import SingleLinkedList, DoubleLinkedList, LinkedList


class TestLinkedList(unittest.TestCase):
    """
    A TestCase class to help ensure the linked list classes are functional.
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.node_types: Tuple[Node] = (SingleLinkNode, DoubleLinkNode)
        self.lst_types: Tuple[LinkedList] = (SingleLinkedList, DoubleLinkedList)

    def test_empty_linked_list(self) -> None:
        """
        Test the creation of an empty linked list object. This method should create a linked
        list with no nodes.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type()
            self.check_assertions_on_empty_linked_list(linked_list)

    def test_single_node_linked_list(self) -> None:
        """
        Test that a single node may be added to a linked list object.

        Returns:
            None
        """
        for node_type, lst_type in zip(self.node_types, self.lst_types):  # type: ignore
            linked_list = lst_type()
            linked_list.head = node_type(5)
            self.assertFalse(linked_list.is_empty)
            self.assertEqual(linked_list.size, 1)
            self.assertEqual("[5]", str(linked_list))
            self.assertEqual("[5]", repr(linked_list))
            self.assertEqual(hash((node_type(5),)), hash(linked_list))

    def test_multiple_node_linked_list(self) -> None:
        """
        Test that multiple nodes may be added to a SingleLinkedList object. This method should
        create a linked list with multiple nodes, and the nodes should be in the order they were
        added.

        Returns:
            None
        """
        linked_list = SingleLinkedList()
        linked_list.head = SingleLinkNode(5)
        linked_list.head.next = SingleLinkNode(6)
        linked_list.head.next.next = SingleLinkNode(7)
        self.assertFalse(linked_list.is_empty)
        self.assertEqual(linked_list.size, 3)
        self.assertEqual("[5, 6, 7]", str(linked_list))
        self.assertEqual("[5, 6, 7]", repr(linked_list))
        self.assertEqual(
            hash((SingleLinkNode(5), SingleLinkNode(6), SingleLinkNode(7))),
            hash(linked_list),
        )

    def test_init_from_args(self) -> None:
        """
        Test the __init__ method of the SingleLinkedList class when it is initialized with
        arguments. This method should create a linked list with the given arguments as the data of
        the nodes.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6, 7)
            self.assertEqual(linked_list.size, 3)
            self.assertEqual("[5, 6, 7]", str(linked_list))
            self.assertEqual("[5, 6, 7]", repr(linked_list))
            self.assertEqual(hash((Node(5), Node(6), Node(7))), hash(linked_list))

    def test_linked_list_equality(self) -> None:
        """
        Test the equality of SingleLinkedList objects.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list1 = lst_type(5, 6, 7)
            linked_list2 = lst_type(5, 6, 7)

            self.assertEqual(linked_list1, linked_list2)
            self.assertNotEqual(linked_list1, lst_type())
            self.assertNotEqual(linked_list1, None)

    def test_linked_list_inequality(self) -> None:
        """
        Test the inequality of SingleLinkedList objects.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list1 = lst_type(5, 6, 7)
            linked_list2 = lst_type(5, 6)

            self.assertNotEqual(linked_list1, linked_list2)
            self.assertNotEqual(linked_list1, lst_type())
            self.assertNotEqual(linked_list1, None)

    def test_insert_at_head(self) -> None:
        """
        Test the insert_at_head method of the SingleLinkedList class. This method should insert
        a node at the head of the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type()
            linked_list.insert_at_head(5)
            self.assertEqual(linked_list.size, 1)
            self.assertEqual("[5]", str(linked_list))
            self.assertEqual("[5]", repr(linked_list))
            self.assertEqual(hash((Node(5),)), hash(linked_list))

    def test_insert_at_tail(self) -> None:
        """
        Test the insert_at_tail method of the SingleLinkedList class. This method should insert
        a node at the tail of the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6)
            linked_list.insert_at_tail(7)
            self.assertEqual(linked_list.size, 3)
            self.assertEqual("[5, 6, 7]", str(linked_list))
            self.assertEqual("[5, 6, 7]", repr(linked_list))
            self.assertEqual(hash((Node(5), Node(6), Node(7))), hash(linked_list))

    def test_insert_at_index(self) -> None:
        """
        Test the insert_at_index method of the SingleLinkedList class. This method should insert
        a node at the given index in the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6, 7)
            linked_list.insert_at_index(4, 1)
            self.assertEqual(linked_list.size, 4)
            self.assertEqual("[5, 4, 6, 7]", str(linked_list))
            self.assertEqual("[5, 4, 6, 7]", repr(linked_list))
            self.assertEqual(
                hash((Node(5), Node(4), Node(6), Node(7))), hash(linked_list)
            )

    def check_assertions_on_empty_linked_list(
        self, linked_list: SingleLinkedList
    ) -> None:
        """
        Check that all the assertions that should be true for an empty linked list are true.

        Args:
            linked_list: The linked list to check.

        Returns:
            None
        """
        # each of these are all valid ways to check if the linked list is empty
        self.assertIsNone(linked_list.head)
        self.assertTrue(linked_list.is_empty)
        self.assertEqual(linked_list.size, 0)

        # the string representation of an empty linked list is an empty list
        self.assertEqual("[]", str(linked_list))
        self.assertEqual("[]", repr(linked_list))

        # the hash of an empty linked list is the hash of an empty tuple
        self.assertEqual(hash(()), hash(linked_list))

    def test_remove_at_head(self) -> None:
        """
        Test the remove_at_head method of the SingleLinkedList class. This method should remove
        the node at the head of the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6, 7)
            linked_list.remove_at_head()
            self.assertEqual(linked_list.size, 2)
            self.assertEqual("[6, 7]", str(linked_list))
            self.assertEqual("[6, 7]", repr(linked_list))
            self.assertEqual(hash((Node(6), Node(7))), hash(linked_list))
            linked_list.remove_at_head()
            self.assertEqual(linked_list.size, 1)
            self.assertEqual("[7]", str(linked_list))
            self.assertEqual("[7]", repr(linked_list))
            self.assertEqual(hash((Node(7),)), hash(linked_list))
            linked_list.remove_at_head()
            self.check_assertions_on_empty_linked_list(linked_list)

    def test_remove_at_tail(self) -> None:
        """
        Test the remove_at_tail method of the SingleLinkedList class. This method should remove
        the node at the tail of the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6, 7)
            linked_list.remove_at_tail()
            self.assertEqual(linked_list.size, 2)
            self.assertEqual("[5, 6]", str(linked_list))
            self.assertEqual("[5, 6]", repr(linked_list))
            self.assertEqual(hash((Node(5), Node(6))), hash(linked_list))
            linked_list.remove_at_tail()
            self.assertEqual(linked_list.size, 1)
            self.assertEqual("[5]", str(linked_list))
            self.assertEqual("[5]", repr(linked_list))
            self.assertEqual(hash((Node(5),)), hash(linked_list))
            linked_list.remove_at_tail()
            self.check_assertions_on_empty_linked_list(linked_list)

    def test_remove_at_index(self) -> None:
        """
        Test the remove_at_index method of the SingleLinkedList class. This method should remove
        the node at the given index in the linked list.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list = lst_type(5, 6, 7)
            linked_list.remove_at_index(1)
            self.assertEqual(linked_list.size, 2)
            self.assertEqual("[5, 7]", str(linked_list))
            self.assertEqual("[5, 7]", repr(linked_list))
            self.assertEqual(hash((Node(5), Node(7))), hash(linked_list))
            del linked_list[1]  # same as remove_at_index, but using the del keyword
            self.assertEqual(linked_list.size, 1)
            self.assertEqual("[5]", str(linked_list))
            self.assertEqual("[5]", repr(linked_list))
            self.assertEqual(hash((Node(5),)), hash(linked_list))
            linked_list.remove_at_index(0)
            self.check_assertions_on_empty_linked_list(linked_list)

    def test_iter(self) -> None:
        """
        Test the __iter__ method of the SingleLinkedList class.

        Returns:
            None
        """
        items = [5, 6, 7]
        for lst_type in self.lst_types:
            linked_list = lst_type(*items)
            self.assertEqual([node.data for node in linked_list], items)

    def test_get_item(self) -> None:
        """
        Test the __getitem__ method of the SingleLinkedList class.

        Returns:
            None
        """
        items = [5, 6, 7]
        for lst_type in self.lst_types:
            linked_list = lst_type(*items)
            for i in range(3):
                self.assertEqual(linked_list[i], items[i])
            with self.assertRaises(IndexError):
                print(
                    linked_list[3]
                )  # should raise an IndexError because the index is out of bounds

    def test_linked_list_comparison(self) -> None:
        """
        Test the comparison of SingleLinkedList objects.

        Returns:
            None
        """
        for lst_type in self.lst_types:
            linked_list_1 = lst_type(5, 6, 7)
            linked_list_2 = lst_type(5, 6, 8)

            self.assertLessEqual(linked_list_1, linked_list_2)
            self.assertGreaterEqual(linked_list_2, linked_list_1)
            # modify linked_list_1 to be less than linked_list_2
            linked_list_1[0], linked_list_1[1] = 4, 5
            self.assertLess(linked_list_1, linked_list_2)
            self.assertGreater(linked_list_2, linked_list_1)

    def test_get_items_index_slicing(self) -> None:
        """
        Test the index slicing of SingleLinkedList objects. This method should return the
        appropriate sublist of the linked list. However, it is important to note two major points:

        1. The slicing does not modify the original linked list, or return a new linked list; it
        returns a list of the nodes at the given indices.
        2. This is not a typical operation for a linked list, but it is useful for testing and
        illustrating how a linked list can be sliced.

        How is this possible? The __getitem__ method of the SingleLinkedList class is implemented
        to return a list of the nodes at the given indices (see "if isinstance(item, slice)").

        Returns:
            None
        """
        items = [5, 6, 7, 8, 9]
        for lst_type in self.lst_types:
            linked_list = lst_type(*items)
            self.assertEqual(items[0:2], linked_list[0:2])
            self.assertEqual(items[1:], linked_list[1:])
            self.assertEqual(items[:2], linked_list[:2])
            self.assertEqual(items[:], linked_list[:])
            self.assertEqual(items[1:1], linked_list[1:1])
            self.assertEqual(items[1:0], linked_list[1:0])
            self.assertEqual(items[1:3], linked_list[1:3])

    def test_set_items_index_slicing(self) -> None:
        """
        Test the setting of items using index slicing in SingleLinkedList objects. This method
        should set the nodes at the given indices to the given values. However, it is important to
        note two major points:

        1. The slicing does modify the original linked list; it sets the nodes at the given
        indices to the given values.
        2. This is not a typical operation for a linked list, but it is useful for testing and
        illustrating how a linked list can be sliced.

        How is this possible? The __setitem__ method of the SingleLinkedList class is implemented
        to set the nodes at the given indices to the given values (see "if isinstance(key, slice)").

        Returns:
            None
        """
        items = [5, 6, 7, 8, 9]
        for lst_type in self.lst_types:
            linked_list = lst_type(*items)
            linked_list[0:2] = [4, 5]
            self.assertEqual("[4, 5, 7, 8, 9]", str(linked_list))
            linked_list[1:] = [6, 7, 8, 9]
            self.assertEqual("[4, 6, 7, 8, 9]", str(linked_list))
            linked_list[:2] = [5, 6]
            self.assertEqual("[5, 6, 7, 8, 9]", str(linked_list))
            linked_list[:] = [5, 6, 7, 8, 9]
            self.assertEqual("[5, 6, 7, 8, 9]", str(linked_list))
            linked_list[1:1] = [6]
            self.assertEqual("[5, 6, 7, 8, 9]", str(linked_list))
            linked_list[1:0] = [6]
            self.assertEqual("[5, 6, 7, 8, 9]", str(linked_list))
            linked_list[1:3] = [6, 7]
            self.assertEqual("[5, 6, 7, 8, 9]", str(linked_list))


if __name__ == "__main__":
    unittest.main()
