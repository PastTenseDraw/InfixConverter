#
from Node import Node

class Stack:
    def __init__(self):
        self.tos = None

    def push(self, item):
        head = Node(item, self.tos)
        self.tos = head


    def pop(self):
        new_head = self.tos.next
        old_head = self.tos
        self.tos.next = None
        self.tos = new_head
        return old_head

    def top(self):
        return self.tos.data

    def size(self):
        size = 0
        reference = self.tos
        while reference.next is not None:
            reference = reference.next
            size += 1
        return size

    def empty_stack(self):

        return self.tos is None