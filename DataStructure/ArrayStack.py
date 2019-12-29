from ArrayList import ArrayList


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.append(e)

    def pop(self):
        if self.is_empty():
            return Exception("Stack is Empty")
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return Exception("Stack is Empty")
        return self.data[-1]
