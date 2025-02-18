"""
Module for the implementation of linked lists.

This code simplifies the subsequent import statements in other modules. For example, instead of
importing the LinkedList class from the abstract module, you can import it directly from the
linked_list module.

Classes:
    LinkedList: An abstract class for linked lists; offers common methods for linked lists.
    SingleLinkedList: A singly linked list, where each node has a reference to the next node.
    DoubleLinkedList: A doubly linked list, where each node has a reference to the next and previous
        nodes.
"""

from .abstract import LinkedList
from .impl import SingleLinkedList, DoubleLinkedList

__all__ = ["LinkedList", "SingleLinkedList", "DoubleLinkedList"]
