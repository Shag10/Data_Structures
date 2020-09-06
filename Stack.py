from collections import deque

class Stack:
    def __init__(self):
        self.contain = deque()

    def push(self, val):
        self.contain.append(val)

    def pop(self):
        return self.contain.pop()

    def peek(self):
        return self.contain[-1]

    def is_empty(self):
        return len(self.contain) == 0

    def length(self):
        return len(self.contain)


if __name__ == "__main__":
    stack = Stack()
    stack.push(523)
    stack.push(620)
    print(stack.peek())
    stack.pop()
    print("After poping", stack.peek())
