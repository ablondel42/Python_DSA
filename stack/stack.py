class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackList:
    def __init__(self):
        self.stack = []

    def print_stack(self):
        for i in range(len(self.stack)-1, -1, -1):
            print(self.stack[i])

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()



class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp


def is_balanced_parentheses(brackets):
    stack = StackList()

    for b in brackets:
        if b == '(':
            stack.push(b)
        elif b == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()


def sort_stack(stack):
    sorted_stack = StackList()

    while not stack.is_empty():
        top = stack.pop()
        while not sorted_stack.is_empty() and sorted_stack.peek() > top:
            stack.push(sorted_stack.pop())
        sorted_stack.push(top)
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())

