"""
This module contains an abstract base class for linked lists. The linked list may be iterated over
to access each node in the list. It also provides a string representation of the linked list.

Some operations, such as queries or modifying operations, are not implemented in this class.
Instead, they are implemented in the concrete classes that inherit from this class. This is because
the implementation of these operations may differ between linked list types, such as singly linked
lists and doubly linked lists.
"""

import abc
from typing import Union, List

from node import (
    Node,
    SingleLinkNode,
    DoubleLinkNode,
)  # this is the Node class from the node.py module we created


class LinkedList(abc.ABC):
    """
    An abstract base class for linked lists. This class is not meant to be instantiated directly.
    It defines the common interface for linked lists, such as inserting, removing, and searching
    for nodes in the list. The linked list may be iterated over to access each node in the list. It
    also provides a string representation of the linked list.
    """

    def __init__(self, *args) -> None:
        self.head: Union[None, SingleLinkNode, DoubleLinkNode] = (
            None  # all linked lists have a head node
        )
        for data in args:
            self.insert_at_tail(data)

    def __iter__(self) -> iter:
        curr: Union[None, SingleLinkNode, DoubleLinkNode] = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    def __getitem__(self, key) -> Union[Node, List[Node]]:
        """
        Get the node at the given index in the linked list.

        Args:
            key: The index of the node to get.

        Returns:
            The node at the given index in the linked list.
        """
        if isinstance(key, slice):
            indices = range(*key.indices(self.size))
            return [self[idx] for idx in indices]

        if key < 0:
            raise IndexError("Index must be non-negative.")

        for idx, node in enumerate(self):
            if idx == key:
                if isinstance(node, Node):
                    return node
                raise TypeError(
                    "Node is not of type Node; something has gone terribly wrong!"
                )

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(
            f"Index {key} does not exist for {type(self).__name__} of size {self.size}."
        )

    def __setitem__(self, key, value) -> None:
        """
        Set the data of the node at the given index in the linked list. This allows for the use of
        the assignment operator to set the data of a node at a specific index. For example, if
        linked_list is a SingleLinkedList object, then linked_list[0] = 5 will set the data of the
        node at index 0 to 5. If the index is out of bounds, an IndexError is raised.
        Args:
            key: The index of the node to set.
            value: The data to set the node to.

        Returns:
            None
        """
        if isinstance(key, slice):
            indices = range(*key.indices(self.size))
            for value_idx, lst_idx in enumerate(
                indices
            ):  # this is a recursive call to __setitem__
                self[lst_idx] = value[value_idx]
            return

        if key < 0:
            raise IndexError("Index must be non-negative.")

        for idx, node in enumerate(self):
            if idx == key:
                node.data = value
                return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(
            f"Index {key} does not exist for {type(self).__name__} of size {self.size}."
        )

    def __delitem__(self, key) -> None:
        """
        Delete the node at the given index in the linked list. This allows for the use of the del
        keyword to delete a node at a specific index.

        For example, if linked_list is a SingleLinkedList object, then del linked_list[0] will
        delete the node at index 0, rather than having to call linked_list.remove_at_index(0).

        Args:
            key: The index of the node to delete.

        Returns:
            None
        """
        self.remove_at_index(index=key)

    def __str__(self) -> str:
        """
        The string representation of the linked list is the string representation of the data in
        each node separated by commas and enclosed in square brackets.

        Returns:
            The string representation of the linked list.
        """
        return str([node.data for node in self])

    def __repr__(self) -> str:
        """
        The string representation of the linked list is the string representation of the data in
        each node separated by commas and enclosed in square brackets.

        Returns:
            The string representation of the linked list.
        """
        return str(self)

    def __relation(self, other, constraint) -> bool:
        """
        A generic inequality comparison method which may accept a function to compare two nodes.
        When the function returns True, the binary relation is satisfied (e.g., equality).

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:

        """
        if isinstance(other, LinkedList) and self.size == other.size:
            for node_1, node_2 in zip(self, other):
                if not constraint(node_1, node_2):  # if constraint is not satisfied
                    return False  # a pair of nodes satisfy the binary relation
            return True  # the given func was never True for any pair of nodes
        return False  # default to False if other is not a SingleLinkedList

    def __eq__(self, other) -> bool:
        """
        Every node in the linked list must be equal to the corresponding node in the
        other linked list. If the linked lists are not the same size, this method returns False.

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:
            True if every node in the list is equal to the corresponding node in the other list.
            False otherwise.
        """
        return self.__relation(other, lambda node_1, node_2: node_1 == node_2)

    def __ne__(self, other) -> bool:
        """
        Every node in the linked list must not be equal to the corresponding node in the
        other linked list. If the linked lists are not the same size, this method returns True.

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:
            True if any node in this linked list is not equal to the corresponding node in the
            other linked list. False otherwise.
        """
        return not self == other  # use the __eq__ method to determine inequality

    def __lt__(self, other) -> bool:
        """
        Every node in the linked list must be less than the corresponding node in the other
        linked list. If the linked lists are not the same size, this method returns False.

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:
            True if every node in this linked list is less than the corresponding node in the
            other linked list. False otherwise.
        """
        return self.__relation(other, lambda node_1, node_2: node_1 < node_2)

    def __le__(self, other) -> bool:
        """
        Every node in the linked list must be less than or equal to the corresponding node in
        the other linked list. If the linked lists are not the same size, this method returns False.
        Args:
            other:

        Returns:

        """
        return self.__relation(other, lambda node_1, node_2: node_1 <= node_2)

    def __gt__(self, other) -> bool:
        """
        Every node in the list must be greater than the corresponding node in the other list. If
        the linked lists are not the same size, this method returns False.

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:
            True if every node in the list is greater than the corresponding node in the other list.
            False otherwise.
        """
        return self.__relation(other, lambda node_1, node_2: node_1 > node_2)

    def __ge__(self, other) -> bool:
        """
        Every node in the list must be greater than or equal to the corresponding node in
        the other list.

        Args:
            other: The other SingleLinkedList to compare to.

        Returns:
            True if every node in the list is greater than or equal to the corresponding node in
            the other list. False otherwise.
        """
        return self.__relation(other, lambda node_1, node_2: node_1 >= node_2)

    def __hash__(self) -> int:
        """
        The hash of the linked list is the hash of the tuple of the nodes.

        Returns:
            The hash of the linked list.
        """
        return hash(tuple(self))

    @property
    def size(self) -> int:
        """
        Get the number of nodes in the linked list.

        Returns:
            The number of nodes in the linked list.
        """
        count: int = 0
        for _ in self:  # we can use the __iter__ method to iterate over the nodes
            count += 1
        return count

    @property
    def is_empty(self) -> bool:
        """
        Simple and efficient check to see if the linked list is empty.

        Returns:
            True if the linked list is empty, False otherwise.
        """
        return self.head is None

    @abc.abstractmethod
    def insert_at_tail(self, data: object) -> None:
        """
        Insert a new node with the given data at the tail of the linked list.

        Args:
            data: Any data to store in the new node to insert.

        Returns:
            None
        """

    @abc.abstractmethod
    def remove_at_tail(self) -> None:
        """
        Remove the node at the tail of the linked list, if it exists.

        Returns:
            None
        """

    @abc.abstractmethod
    def insert_at_head(self, data: object) -> None:
        """
        Insert a new node with the given data at the head of the linked list.

        Args:
            data: Any data to store in the new node to insert.

        Returns:
            None
        """

    @abc.abstractmethod
    def remove_at_head(self) -> None:
        """
        Remove the node at the head of the linked list, if it exists.

        Returns:
            None
        """

    @abc.abstractmethod
    def insert_at_index(self, data: object, index: int) -> None:
        """
        Insert a new node with the given data at the specified index in the linked list.

        Args:
            data: Any data to store in the new node to insert.
            index: The index at which to insert the new node.

        Returns:
            None
        """

    @abc.abstractmethod
    def remove_at_index(self, index: int) -> None:
        """
        Remove the node at the specified index in the linked list.

        Args:
            index: The index of the node to remove.

        Returns:
            None
        """
