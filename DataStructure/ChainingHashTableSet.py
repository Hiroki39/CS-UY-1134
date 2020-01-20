import random
import ctypes
from DoublyLinkedList import DoublyLinkedList


def make_array(n):
    return (n * ctypes.py_object)()


class ChainingHashTableSet:
    class MADHashFunction:  # h2 = (a * h1(k) + b) % p) % N
        def __init__(self, N, p=40206835204840513073):  # p is a large prime greater than 2^64
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    def __init__(self, N=64):
        self.N = N
        # Cannot use ArrayList since items are set randomly
        self.table = make_array(N)
        for i in range(self.N):
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.hash_function = ChainingHashTableSet.MADHashFunction(self.N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def add(self, key):
        if key not in self:
            i = self.hash_function(key)
            self.table[i].add_last(key)
            self.n += 1
            if self.n > self.N:
                self.rehash(2 * self.N)

    def remove(self, key):
        if key not in self:
            raise KeyError(key + " not found")
        i = self.hash_function(key)
        curr_node = self.table[i].header.next
        while curr_node is not self.table[i].trailer:
            if curr_node.data == key:
                self.table[i].delete_node(curr_node)
                break
            curr_node = curr_node.next
        self.n -= 1
        if self.n < self.N // 4:
            self.rehash(self.N // 2)

    def __contains__(self, key):
        i = self.hash_function(key)
        curr_node = self.table[i].header.next
        while curr_node is not self.table[i].trailer:
            if curr_node.data == key:
                return True
            curr_node = curr_node.next
        return False

    def __iter__(self):
        for i in range(self.N):
            for key in self.table[i]:
                yield key

    def __repr__(self):
        return "{" + ", ".join(str(key) for key in self) + "}"

    def rehash(self, new_size):
        old_data = [key for key in self]
        self.__init__(new_size)  # reinitiate ChainingHashTableMap
        for key in old_data:
            self.add(key)

    def intersection(self, other):
        new_set = ChainingHashTableSet()
        for key in self:
            if key in other:
                new_set.add(key)
        return new_set

    def __and__(self, other):
        return self.intersection(other)

    def union(self, other):
        new_set = ChainingHashTableSet()
        for key in self:
            new_set.add(key)
        for key in other:
            if key not in new_set:
                new_set.add(key)
        return new_set

    def __or__(self, other):
        return self.union(other)

    def difference(self, other):
        new_set = ChainingHashTableSet()
        for key in self:
            if key not in other:
                new_set.add(key)
        return new_set

    def __sub__(self, other):
        return self.difference(other)
