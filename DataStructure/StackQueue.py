from ArrayStack import ArrayStack


class StackQueue:
    def __init__(self):
        self.instack = ArrayStack()
        self.outstack = ArrayStack()

    def __len__(self):
        return len(self.instack) + len(self.outstack)

    def is_empty(self):
        return self.instack.is_empty() and self.outstack.is_empty()

    def enqueue(self, item):
        self.instack.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.outstack.is_empty():
            for i in range(len(self.instack)):
                self.outstack.push(self.instack.pop())
        return self.outstack.pop()

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.outstack.is_empty():
            for i in range(len(self.instack)):
                self.outstack.push(self.instack.pop())
        return self.outstack.top()
