#

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
