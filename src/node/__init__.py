"""
Node module for linked list implementation.

This code simplifies the subsequent import statements in other modules. For example, instead of
importing the Node class from the abstract module, you can import it directly from the node module.

Classes:
    Node: A node in a linked list.
    SingleLinkNode: A node in a single linked list.
    DoubleLinkNode: A node in a doubly linked list.
"""

from .abstract import Node
from .impl import SingleLinkNode, DoubleLinkNode

__all__ = ["Node", "SingleLinkNode", "DoubleLinkNode"]