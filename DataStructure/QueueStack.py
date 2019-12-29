from ArrayQueue import ArrayQueue


class QueueStack1:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.enqueue(e)

    def pop(self, e):
        for i in range(len(self.data) - 1):
            value = self.data.dequeue()
            self.data.enqueue(value)
        return self.data.dequeue()

    def top(self, e):
        for i in range(len(self.data) - 1):
            value = self.data.dequeue()
            self.data.enqueue(value)
        value = self.data.dequeue()
        self.data.enqueue(value)
        return value


class QueueStack2:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.enqueue(e)
        for i in range(len(self.data - 1)):
            self.data.enqueue(self.data.dequeue())

    def pop(self, e):
        return self.data.dequeue()

    def top(self, e):
        return self.data.first()
