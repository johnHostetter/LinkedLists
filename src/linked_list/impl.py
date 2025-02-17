"""
This module contains the SingleLinkedList class that represents a singly linked list.
"""

from typing import Union, Tuple

# these are the custom classes that we will use in the linked list
from node import Node, SingleLinkNode
from linked_list import LinkedList

class SingleLinkedList(LinkedList):
    """
    A singly linked list. Each node in the linked list has a reference to the next node in the
    list. The linked list itself has a reference to the head node.

    If the linked list is empty, the head is None.

    The linked list may be iterated over to access each node in the list.

    An object of SingleLinkedList can be compared to other linked lists for equality, inequality,
    less than, less than or equal to, greater than, greater than or equal to, and hashed.
    """

    def __last_node(self) -> Tuple[Union[None, SingleLinkNode], Union[None, SingleLinkNode]]:
        """
        Get the last node and the node before the last node in the linked list.

        Returns:
            The last node and the node before the last node in the linked list. If the list is
            empty, both values are None. If the list has only one node, the second value is None.
            If the list has two or more nodes, both values are not None.
        """
        curr: Union[None, SingleLinkNode] = self.head
        predecessor: Union[None, SingleLinkNode] = None

        if curr is None:
            return curr, predecessor

        while curr.next is not None:
            predecessor = curr
            curr = curr.next
        return curr, predecessor

    def insert_at_head(
        self, data: object
    ) -> None:  # I will give this method to the class
        """
        Insert a new node with the given data at the head of the linked list.

        Args:
            data: Any data to store in the new node to insert.

        Returns:
            None
        """
        if isinstance(data, Node):
            raise ValueError(
                "Cannot insert a Node object. "
                "Insert the data instead if this was intended behavior."
            )

        new_node = SingleLinkNode(data)
        new_node.next = self.head
        self.head = new_node

    def remove_at_head(self) -> None:  # I will ask the class to implement this method
        """
        Remove the node at the head of the linked list, if it exists.

        Returns:
            None
        """
        if self.head is not None:
            self.head = self.head.next

    def insert_at_tail(self, data) -> None:
        """
        Insert a new node with the given data at the tail of the linked list.

        Args:
            data: Any data to store in the new node to insert.

        Returns:
            None
        """
        new_node: SingleLinkNode = SingleLinkNode(data)
        if self.head is None:
            self.head = new_node
            return

        last_node, _ = self.__last_node()
        last_node.next = new_node

    def remove_at_tail(self) -> None:
        # base case of empty list
        if self.head is None:
            return

        # base case of single node list
        if self.head.next is None:
            self.head = None
            return

        # general case
        _, next_to_last = self.__last_node()
        next_to_last.next = None

    def insert_at_index(self, data: object, index: int) -> None:
        if index < 0:
            raise IndexError("Index must be non-negative.")

        if index == 0:
            self.insert_at_head(data)
            return

        for idx, node in enumerate(self):
            if idx == index - 1:
                new_node = SingleLinkNode(data)
                new_node.next = node.next
                node.next = new_node
                return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(
            f"Index {index} does not exist for {type(self).__name__} of size {self.size}."
        )

    def remove_at_index(self, index: int) -> None:
        if index < 0:
            raise IndexError("Index must be non-negative.")

        if index == 0:
            self.remove_at_head()
            return

        for idx, node in enumerate(self):
            if idx == index - 1:
                if node.next is not None:
                    node.next = node.next.next
                    return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(
            f"Index {index} does not exist for {type(self).__name__} of size {self.size}."
        )
