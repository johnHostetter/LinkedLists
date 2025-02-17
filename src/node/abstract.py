"""
This module contains the Node class, which is used to create nodes in a linked-based memory
structure. It may be extended to create nodes in linked lists, trees, and other data structures.
"""


class Node:
    """
    A node in linked-based memory structure. Each node has a reference to some data it stores,
    and does not contain any references to other nodes. Other classes that inherit from this class
    will define references to other nodes.

    In the context of a doubly linked list, the prev attribute is used to reference the node
    before the current node. For all types of linked lists, the next attribute is used to reference
    the node after the current node.

    Attributes:
        data: The data stored in the node.
    """

    def __init__(self, data: object) -> None:
        self.data: object = data  # can store any data

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
