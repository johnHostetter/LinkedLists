"""
This module contains the Node class, which is used to create nodes in a linked list.s
"""
from typing import Union


class Node:
    """
    A node in a linked list. Each node has a reference to the data it stores, the node before it,
    and the node after it. If there is no node before or after it, the reference is None.

    In the context of a single linked list, the prev attribute is not used. In the context of a
    doubly linked list, the prev attribute is used to reference the node before the current node.
    For all types of linked lists, the next attribute is used to reference the node after the
    current node.

    Attributes:
        data: The data stored in the node.
        prev: The node before this one in the linked list.
        next: The node after this one in the
    """
    def __init__(self, data: object) -> None:
        self.data: object = data  # can store any data
        self.prev: Union[None, Node] = (
            None  #  either keep a reference to a node or None
        )
        self.next: Union[None, Node] = None

    def __str__(self) -> str:
        return str(self.data)

    def __repr__(self) -> str:
        return str(self.data)

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data == other.data
        return self.data == other

    def __ne__(self, other) -> bool:
        return not self == other  # use the __eq__ method to determine inequality

    def __lt__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data < other.data
        return self.data < other

    def __le__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data <= other.data
        return self.data <= other

    def __gt__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data > other.data
        return self.data > other

    def __ge__(self, other) -> bool:
        if isinstance(other, Node):
            return self.data >= other.data
        return self.data >= other

    def __hash__(self) -> int:
        return hash(self.data)
