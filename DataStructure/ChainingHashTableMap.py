import random
import ctypes
from UnsortedArrayMap import UnsortedArrayMap


def make_array(n):
    return (n * ctypes.py_object)()


class ChainingHashTableMap:
    class MADHashFunction:  # h2 = (a * h1(k) + b) % p) % N
        def __init__(self, N, p=40206835204840513073):  # p is a large prime greater than 2^64
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self, N=64):
        self.N = N
        # Cannot use ArrayList since items are set randomly
        self.table = make_array(N)
        for i in range(self.N):   # Attribute for Homework9:
            # Use Item for single key, use UnsortedArrayMap for more than 1 keys
            self.table[i] = None
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(self.N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.hash_function(key)
        if self.table[i] is None:
            raise KeyError(str(key) + " not found")
        elif isinstance(self.table[i], ChainingHashTableMap.Item):
            if self.table[i].key != key:
                raise KeyError(str(key) + " not found")
            return self.table[i].value
        return self.table[i][key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            self.table[i] = ChainingHashTableMap.Item(key, value)
            self.n += 1
        elif isinstance(self.table[i], ChainingHashTableMap.Item):
            if self.table[i].key != key:
                old_item = self.table[i]
                self.table[i] = UnsortedArrayMap()
                self.table[i][old_item.key] = old_item.value
                self.table[i][key] = value
                self.n += 1
            else:
                self.table[i].value = value
        else:
            old_size = len(self.table[i])
            self.table[i][key] = value
            if len(self.table[i]) > old_size:
                self.n += 1
        if self.n > self.N:
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        if self.table[i] is None:
            raise KeyError(str(key) + " not found")
        elif isinstance(self.table[i], ChainingHashTableMap.Item):
            if self.table[i].key != key:
                raise KeyError(str(key) + " not found")
            self.table[i] = None
        else:
            del self.table[i][key]
            if len(self.table) == 1:
                self.table[i] = ChainingHashTableMap.Item(
                    self.table[i].table[0].key, self.table[i].table[0].value)
        self.n -= 1
        if self.n < self.N // 4:
            self.rehash(self.N // 2)

    def __iter__(self):
        for i in range(self.N):
            if self.table[i] is not None:
                if isinstance(self.table[i], ChainingHashTableMap.Item):
                    yield self.table[i].key
                else:
                    for key in self.table[i]:
                        yield key

    def __repr__(self):
        return "{" + ", ".join(str(key) + ": " + str(self[key]) for key in self) + "}"

    def rehash(self, new_size):
        old_data = [(key, self[key]) for key in self]
        self.__init__(new_size)  # Reinitiate ChainingHashTableMap
        for key, value in old_data:
            self[key] = value
