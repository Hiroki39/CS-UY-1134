import random
import ctypes
import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from DoublyLinkedList import DoublyLinkedList
from UnsortedArrayMap import UnsortedArrayMap


def make_array(n):
    return (n * ctypes.py_object)()


class LinkedHashTableMap:  # modified version of ChainingHashTableMap for FIFO order in __iter__
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
            self.value = value  # a value or a node containing key and value

    def __init__(self, N=64):
        self.N = N
        # Cannot use ArrayList since items are set randomly
        self.table = make_array(N)
        for i in range(self.N):
            # Use Item for single key, use UnsortedArrayMap for more than 1 keys
            self.table[i] = None
        self.n = 0
        self.hash_function = LinkedHashTableMap.MADHashFunction(self.N)
        self.keylist = DoublyLinkedList()

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        i = self.hash_function(key)
        if self.table[i] is None:
            raise KeyError(str(key) + " not found")
        elif isinstance(self.table[i], LinkedHashTableMap.Item):
            if self.table[i].key != key:
                raise KeyError(str(key) + " not found")
            return self.table[i].value.data.value
        return self.table[i][key].data.value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        if self.table[i] is None:
            key_val_node = self.keylist.add_last(
                LinkedHashTableMap.Item(key, value))
            self.table[i] = LinkedHashTableMap.Item(key, key_val_node)
            self.n += 1
        elif isinstance(self.table[i], LinkedHashTableMap.Item):
            if self.table[i].key != key:
                old_item = self.table[i]
                self.table[i] = UnsortedArrayMap()
                self.table[i][old_item.key] = old_item.value
                self.table[i][key] = self.keylist.add_last(
                    LinkedHashTableMap.Item(key, value))
                self.n += 1
            else:
                self.table[i].value.data.value = value
        else:
            try:
                self.table[i][key].data.value = value
            except KeyError:
                self.table[i][key] = self.keylist.add_last(
                    LinkedHashTableMap.Item(key, value))
                self.n += 1
        if self.n > self.N:
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        if self.table[i] is None:
            raise KeyError(str(key) + " not found")
        elif isinstance(self.table[i], LinkedHashTableMap.Item):
            if self.table[i].key != key:
                raise KeyError(str(key) + " not found")
            self.keylist.delete_node(self.table[i].value)
            self.table[i] = None
        else:
            self.keylist.delete_node(self.table[i][key])
            del self.table[i][key]
            if len(self.table) == 1:
                self.table[i] = LinkedHashTableMap.Item(
                    self.table[i].table[0].key, self.table[i].table[0].value)
        self.n -= 1
        if self.n < self.N // 4:
            self.rehash(self.N // 2)

    def __iter__(self):
        for item in self.keylist:
            yield item.key

    def __repr__(self):
        return "{" + ", ".join(str(key) + ": " + str(self[key]) for key in self) + "}"

    def rehash(self, new_size):
        old_data = [(key, self[key]) for key in self]
        self.__init__(new_size)  # reinitiate LinkedHashTableMap
        for key, value in old_data:
            self[key] = value
