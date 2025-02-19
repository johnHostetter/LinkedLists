"""
This module contains the SingleLinkedList class that represents a singly linked list.
"""

from typing import Union

# these are the custom classes that we will use in the linked list
from node.abstract import Node
from node.impl import DoubleLinkNode
from linked_list.impl.single import SingleLinkedList


class DoubleLinkedList(SingleLinkedList):
    """
    A doubly linked list. Each node in the linked list has a reference to the next node and the
    previous node in the list. The linked list itself has a reference to the head node, and for
    efficiency, the tail node (not required but is more performant).

    If the linked list is empty, the head and tail are None.

    The linked list may be iterated over to access each node in the list (in either direction).

    An object of DoubleLinkedList can be compared to other linked lists for equality, inequality,
    less than, less than or equal to, greater than, greater than or equal to, and hashed.
    """

    def __init__(self, *args):
        self.tail: Union[None, DoubleLinkNode] = (
            None  # order matters here, *args may define tail
        )
        super().__init__(*args)

    def insert_at_head(self, data: object) -> None:
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

        new_node = DoubleLinkNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node  # if the list was empty, the tail is also the head
        self.head = new_node

    def remove_at_head(self) -> None:
        """
        Remove the node at the head of the linked list, if it exists.

        Returns:
            None
        """
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def insert_at_tail(self, data: object) -> None:
        """
        Insert a new node with the given data at the tail of the linked list.

        Args:
            data: Any data to store in the new node to insert.

        Returns:
            None
        """
        new_node: DoubleLinkNode = DoubleLinkNode(data)
        if self.is_empty:
            self.head, self.tail = new_node, new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_at_tail(self) -> None:
        # base case of empty list
        if self.head is None:
            return

        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            # if the tail is None, the list is empty
            self.head = None

    def insert_at_index(self, data: object, index: int) -> None:
        if index < 0:
            raise IndexError("Index must be non-negative.")

        if index == 0:
            self.insert_at_head(data)
            return

        for idx, node in enumerate(self):
            if idx == index - 1:
                new_node = DoubleLinkNode(data)
                new_node.next = node.next
                new_node.prev = node
                if node.next is not None:
                    node.next.prev = new_node
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
                    if node.next is not None:
                        node.next.prev = node
                    return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(
            f"Index {index} does not exist for {type(self).__name__} of size {self.size}."
        )
