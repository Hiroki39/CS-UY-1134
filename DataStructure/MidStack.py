from DoublyLinkedList import DoublyLinkedList


class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.middle = self.data.header

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        self.data.add_last(e)
        if len(self) % 2 == 1:
            self.middle = self.middle.next

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self) % 2 == 1:
            self.middle = self.middle.prev
        return self.data.delete_last()

    def mid_push(self, e):
        if self.is_empty():
            raise Exception("MidStack is empty")
        self.data.add_after(self.middle, e)
        if len(self) % 2 == 1:
            self.middle = self.middle.next
