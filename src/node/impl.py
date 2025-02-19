"""
This module contains both SingleLinkNode and DoubleLinkNode classes, which are used to create nodes
in a single and doubly linked list, respectively.
"""

from typing import Union

# note: both "src.node.abstract import Node" and "from node.abstract import Node" are valid,
# but will change isinstance behavior depending on the import statement used; stay consistent
from node.abstract import Node


class SingleLinkNode(Node):
    """
    A node in a single linked list. Each node has a reference to the data it stores, and the node
    after it. If there is no node after it, the reference is None.

    Attributes:
        data: The data stored in the node.
        next: The node after this one in the linked list.
    """

    def __init__(self, data: object) -> None:
        super().__init__(data)
        self.next: Union[None, Node] = None


class DoubleLinkNode(SingleLinkNode):
    """
    A node in a doubly linked list. Each node has a reference to the data it stores, the node before
    it, and the node after it. If there is no node before or after it, the reference is None. The
    prev attribute is used to reference the node before the current node. The next attribute is used
    to reference the node after the current node.

    Attributes:
        data: The data stored in the node.
        prev: The node before this one in the linked list.
        next: The node after this one in the linked list.
    """

    def __init__(self, data: object) -> None:
        super().__init__(data)
        self.prev: Union[None, Node] = None
