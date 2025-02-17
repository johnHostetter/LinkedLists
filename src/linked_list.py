"""
This module contains the SingleLinkedList class that represents a singly linked list.
"""
from typing import Union, Tuple

from node import Node  # this is the Node class from the node.py module we created


class SingleLinkedList:
    """
    A singly linked list. Each node in the linked list has a reference to the next node in the
    list. The linked list itself has a reference to the head node.

    If the linked list is empty, the head is None.

    The linked list may be iterated over to access each node in the list.

    An object of SingleLinkedList can be compared to other linked lists for equality, inequality,
    less than, less than or equal to, greater than, greater than or equal to, and hashed.
    """
    def __init__(self, *args) -> None:
        self.head: Union[None, Node] = None
        for data in args:
            self.insert_at_tail(data)

    def __iter__(self) -> iter:
        curr: Union[None, Node] = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    def __getitem__(self, item) -> Node:
        """
        Get the node at the given index in the linked list.

        Args:
            item: The index of the node to get.

        Returns:
            The node at the given index in the linked list.
        """
        if item < 0:
            raise IndexError("Index must be non-negative.")

        for idx, node in enumerate(self):
            if idx == item:
                if isinstance(node, Node):
                    return node
                raise TypeError("Node is not of type Node; something has gone terribly wrong!")

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(f"Index {item} does not exist for {type(self).__name__} of size {self.size}.")

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
        if key < 0:
            raise IndexError("Index must be non-negative.")

        for idx, node in enumerate(self):
            if idx == key:
                node.data = value
                return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(f"Index {key} does not exist for {type(self).__name__} of size {self.size}.")

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
        if isinstance(other, SingleLinkedList) and self.size == other.size:
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

    def __last_node(self) -> Tuple[Union[None, Node], Union[None, Node]]:
        """
        Get the last node and the node before the last node in the linked list.

        Returns:
            The last node and the node before the last node in the linked list. If the list is
            empty, both values are None. If the list has only one node, the second value is None.
            If the list has two or more nodes, both values are not None.
        """
        curr: Union[None, Node] = self.head
        predecessor: Union[None, Node] = None

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

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_at_head(self) -> None:  # I will ask the class to implement this method
        if self.head is not None:
            self.head = self.head.next

    def insert_at_tail(self, data) -> None:
        new_node: Node = Node(data)
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
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
                return

        # if we reach this point, the index is out of bounds (i.e., greater than the list's size)
        raise IndexError(f"Index {index} does not exist for {type(self).__name__} of size {self.size}.")

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
        raise IndexError(f"Index {index} does not exist for {type(self).__name__} of size {self.size}.")
