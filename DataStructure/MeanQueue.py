from ArrayQueue import ArrayQueue


class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.curr_sum = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, e):
        if not isinstance(e, (int, float)):
            raise TypeError("could only enqueue int or float")
        self.data.enqueue(e)
        self.curr_sum += e

    def dequeue(self):
        e = self.data.dequeue()
        self.curr_sum -= e
        return e

    def first(self):
        return self.data.first()

    def sum(self):
        return self.curr_sum

    def mean(self):
        if self.is_empty():
            raise Exception("MeanQueue is empty")
        return self.curr_sum / len(self)
