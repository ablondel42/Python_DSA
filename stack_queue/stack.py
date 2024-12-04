class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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

stack = Stack(1)
stack.push(2)
stack.push(3)

p = stack.pop()
print(f"{p.value} removed\n")
p = stack.pop()
print(f"{p.value} removed\n")
p = stack.pop()
print(f"{p.value} removed\n")

stack.print_stack()