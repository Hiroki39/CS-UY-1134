import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from ArrayDeque import ArrayDeque
from ArrayStack import ArrayStack


class MidStack:
    def __init__(self):
        self.part1 = ArrayStack()
        self.part2 = ArrayDeque()

    def is_empty(self):
        return self.part1.is_empty() and self.part2.is_empty()

    def __len__(self):
        return len(self.part1) + len(self.part2)

    def push(self, e):
        self.part2.enqueue_last(e)
        if len(self.part1) < len(self.part2):
            self.part1.push(self.part2.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if self.part2.is_empty():
            return self.part1.top()
        return self.part2.last()

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        if len(self.part1) > len(self.part2):
            self.part2.enqueue_first(self.part1.pop())
        return self.part2.dequeue_last()

    def mid_push(self, e):
        if len(self.part1) > len(self.part2):
            self.part2.enqueue_first(e)
        else:
            self.part1.push(e)
