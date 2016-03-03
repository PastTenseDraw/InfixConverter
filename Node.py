# Node.py

# Name: Drew Baker      Date Assigned: 02/29/16
#
# Course: CSE 1384  Sec H01     Date Due: 03/03/16
#
# File name: Node.py
#
# Program Description: Node class for infix converter.

class Node:
    def __init__(self, item, next):
        self._data = item
        if item == "*" or item == "**" or item == "/" or item == "//" or item == "%":
            self._precedence = 3
        elif item == "+" or item == "-":
            self._precedence = 2
        elif item == ">" or item == "<":
            self._precedence = 1
        elif item == "(" or item == "[":
            self.precedence = 0
        else:
            self.precedence = None
        self._next = next
