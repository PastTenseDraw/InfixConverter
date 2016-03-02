#

class Node:
    def __init__(self, item, next):
        self._data = item
        if item == "*" or "**" or "/" or "//" or "%":
            self._precedence = 2
        elif item == "+" or "-":
            self._precedence = 1
        elif item == "(" or "[":
            self.precedence = 0
        self._next = next
