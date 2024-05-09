#!/usr/bin/python3
"""
A module that defines a class Node, which is a node in a singly linked list
"""


class Node:
    """
    A node object in a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initializing a node object
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = next_node

    @property
    def data(self):
        """
        The data property getter
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        data property setter
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        next_node property getter
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        next_node property setter
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A singly linked list object consisting of nodes
    """

    def __init__(self):
        """
        initialize a singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a node object into the list
        """
        try:
            new_node = Node(value)
        except Exception as ex:
            raise ex
        else:
            if not self.__head:
                self.__head = new_node
            else:
                if self.__head.data >= new_node.data:
                    new_node.next_node = self.__head
                    self.__head = new_node
                else:
                    node = self.__head
                    node_plus = node.next_node
                    while node_plus:
                        if node_plus.data >= new_node.data:
                            break
                        node = node_plus
                        node_plus = node.next_node
                    new_node.next_node = node_plus
                    node.next_node = new_node

    def __str__(self):
        """
        printing the singly_linked list
        """
        ret_string = ""
        node = self.__head
        while node:
            ret_string += "{}\n".format(node.data)
            node = node.next_node
        return (ret_string.strip())
