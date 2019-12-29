class DoublyLinkedList:
    class Node:  # LinkedList Private Node
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):  # For Garbage Collector
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()  # Eliminate Edge Cases
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add_after(self, node, val):  # Constant Time
        new_node = DoublyLinkedList.Node(val, node.next, node)
        node.next.prev = new_node
        node.next = new_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):  # Constant Time
        node.prev.next = node.next
        node.next.prev = node.prev
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
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        curr_node = self.header.next
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next

    def __repr__(self):
        return "[" + "<-->".join([str(elem) for elem in self]) + "]"

    def __getitem__(self, index):
        if not -len(self) <= index <= len(self) - 1:
            raise IndexError("invalid index")
        if index < 0:
            index += len(self)
        cursor = self.header.next
        for i in range(index):
            cursor = cursor.next
        return cursor.data

    def __setitem__(self, index, val):
        if not -len(self) <= index <= len(self) - 1:
            raise IndexError("invalid index")
        if index < 0:
            index += len(self)
        cursor = self.header.next
        for i in range(index):
            cursor = cursor.next
        cursor.data = val
