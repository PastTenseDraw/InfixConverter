# stack.py

# Name: Drew Baker      Date Assigned: 02/29/16
#
# Course: CSE 1384  Sec H01     Date Due: 03/03/16
#
# File name: stack.py
#
# Program Description: Class for the stacks used in the infix converter program.
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