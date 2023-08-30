#!/usr/bin/python3
""" defines a class node"""


class Node:
    """defines the attributes of node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node)) and (value is not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """creates a linked list of nodes"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            hold = self.__head
            while (hold.next_node is not None and hold.next_node.data < value):
                hold = hold.next_node
            new.next_node = hold.next_node
            hold.next_node = new

    def __str__(self):
        values = []
        hold = self.__head
        while hold is not None:
            values.append(str(hold.data))
            hold = hold.next_node
        return ('\n'.join(values))
