class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(value)
        while len(self.stack2):
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next


    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


    def dequeue(self):
        temp = self.first
        if self.length == 0:
            return None
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

