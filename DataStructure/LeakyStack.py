from DoublyLinkedList import DoublyLinkedList
import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class LeakyStack1:
    def __init__(self, n):
        self.data = DoublyLinkedList()
        self.max = n

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def push(self, e):
        self.data.add_last(e)
        if len(self) > self.max:
            self.data.delete_first()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.delete_last()

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.trailer.prev.data


class LeakyStack2:
    def __init__(self, n):
        self.data_arr = make_array(n)
        self.num_of_elems = 0
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        if self.is_empty():
            self.data_arr[0] = item
            self.back_ind = 0
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data_arr)
            self.data_arr[self.back_ind] = item
        if self.num_of_elems < len(self.data_arr):
            self.num_of_elems += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        value = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if self.is_empty():
            self.back_ind = None
        return value

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data[self.back_ind]
