"""
A module to test the SingleLinkedList class.
"""

import unittest
from typing import Tuple

from node import Node, SingleLinkNode, DoubleLinkNode
from linked_list import SingleLinkedList, DoubleLinkedList, LinkedList


class TestLinkedListOptional(unittest.TestCase):
    """
    A TestCase class to help ensure the linked list classes are functional.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.node_types: Tuple[Node] = (SingleLinkNode, DoubleLinkNode)
        self.lst_types: Tuple[LinkedList] = (SingleLinkedList, DoubleLinkedList)

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
