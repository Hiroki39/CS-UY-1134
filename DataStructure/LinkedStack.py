from DoublyLinkedList import DoublyLinkedList


class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        self.data.add_last(e)

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.delete_last()
