class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_after_value(self, value1, value2):
        current = self.head
        while current:
            if current.data == value1:
                new_node = Node(value2)
                new_node.next = current.next
                current.next = new_node
                current = current.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)

llist.insert_after_value(1, 10)
llist.insert_after_value(3, 20)
llist.insert_after_value(5, 30)

llist.print_list()
