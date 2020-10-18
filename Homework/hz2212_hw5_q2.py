import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.maximum = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, elem):
        self.data.push((elem, self.maximum))
        if self.maximum is None or elem > self.maximum:
            self.maximum = elem

    def top(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return_tup = self.data.pop()
        if return_tup[1] is None or return_tup[0] > return_tup[1]:
            self.maximum = return_tup[1]
        return return_tup[0]

    def max(self):
        if self.is_empty():
            raise Exception("MaxStack is empty")
        return self.maximum
