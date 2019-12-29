class SinglyLinkedList:
    class Node:  # LinkedList专属Node
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):  # For Garbage Collector
            self.data = None
            self.next = None

    def __init__(self):
        self.header = SinglyLinkedList.Node()  # Eliminate Edge Cases
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):  # Constant Time
        new_node = SinglyLinkedList.Node(val, node.next)
        node.next = new_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        cursor = self.header
        while cursor.next is not None:
            cursor = cursor.next
        return self.add_after(cursor, val)

    def add_before(self, node, val):
        cursor = self.header
        while cursor.next is not node:
            cursor = cursor.next
        return self.add_after(cursor, val)

    def delete_node(self, node):
        cursor = self.header
        while cursor.next is not node:
            cursor = cursor.next
        cursor.next = node.next
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is Empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is Empty")
        cursor = self.header
        while cursor.next is not None:
            cursor = cursor.next
        return self.delete_node(cursor)

    def __iter__(self):
        cursor = self.header
        while cursor.next is not None:
            yield cursor.next.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " -> ".join([str(elem) for elem in self]) + "]"
