class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head
        if current is not None and current.value == value:
            self.head = current.next
            return
        while current is not None:
            if current.next is not None and current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

node = linked_list.find(2)
print(node.value)

linked_list.delete(2)
node = linked_list.find(2)
print(node)
