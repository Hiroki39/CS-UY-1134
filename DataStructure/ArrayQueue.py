import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, item):  # Constant Time
        if self.num_of_elems == len(self.data_arr):
            self.resize(2 * self.num_of_elems)
        if self.is_empty():
            self.data_arr[0] = item
            self.front_ind = 0
        else:
            back_ind = (self.front_ind +
                        self.num_of_elems) % len(self.data_arr)
            self.data_arr[back_ind] = item
        self.num_of_elems += 1

    def dequeue(self):  # Constant Time
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None  # For Garbage Collector
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        if self.num_of_elems < len(self.data_arr) // 4 and len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY:
            self.resize(len(self.data_arr) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data_arr
        new_data = make_array(new_cap)
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[(
                self.front_ind + new_ind) % len(old_data)]
        self.data_arr = new_data
        self.front_ind = 0
