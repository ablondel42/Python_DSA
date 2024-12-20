class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> ")
            temp = temp.next
        print("None")


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


    def pop(self):
        temp = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp


    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp


    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        temp.next = None
        temp.prev = None
        before.next = after
        after.prev = before
        self.length -= 1
        return temp


    def swap_first_last(self):
        if self.length == 0:
            return None
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp


    def reverse(self):
        if self.length <= 1:
            return
        current = self.head
        while current:
            after = current.next
            current.next = current.prev
            current.prev = after
            current = after
        link = self.head
        self.head = self.tail
        self.tail = link


    def is_palindrome(self):
        if self.length <= 1:
            return True
        left = self.head
        right = self.tail
        while left != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True


dll = DoublyLinkedList(11)
dll.insert(1, 1)
dll.insert(1, 2)
dll.insert(1, 3)

dll.print_list()