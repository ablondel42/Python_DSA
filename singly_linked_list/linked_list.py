class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def get_length(self):
        return self.length


    def print_list(self):
        if self.head:
            temp = self.head
            while temp is not None:
                print(f"({temp.value})", end=" -> ")
                temp = temp.next
        print("None")


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
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
            self.head = new_node
        self.length += 1
        return True


    def pop(self):
        temp = self.head
        pre = temp
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
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
            temp.next = None
        self.length -= 1
        return temp


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp


    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return slow == fast


    def find_kth_from_end(self, k):
        slow = self.head
        fast = self.head
        if k < 0 or self.head is None:
            return None
        if k == 1:
            return self.tail
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


    def partition_list(self, x):
        if self.head is None:
            return
        lesser = LinkedList(-1)
        lesser_tail = lesser.head
        greater = LinkedList(-1)
        greater_tail = greater.head
        temp = self.head

        while temp:
            self.head = self.head.next
            current = temp
            temp = temp.next
            current.next = None

            if current.value < x:
                lesser_tail.next = current
                lesser_tail = current
            else:
                greater_tail.next = current
                greater_tail = current

        lesser.head = lesser.head.next
        greater.head = greater.head.next

        if lesser.head is not None:
            lesser_tail.next = greater.head
            self.head = lesser.head
        else:
            self.head = greater.head


    def remove_duplicates(self):
        seen = set()
        if self.head is None or self.head.next is None:
            return
        prev = None
        current = self.head

        while current:
            if current.value in seen:
                prev.next = current.next
            else:
                seen.add(current.value)
                prev = current
            current = current.next


    def reverse_between(self, start_index, end_index):
        pass