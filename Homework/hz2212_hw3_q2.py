import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, index):
        if not -self.n <= index <= self.n - 1:
            raise IndexError("invalid index")
        if (index < 0):
            return self.data_arr[self.n + index]
        return self.data_arr[index]

    def __setitem__(self, index, val):
        if not -self.n <= index <= self.n - 1:
            raise IndexError("invalid index")
        if index < 0:
            self.data_arr[self.n + index] = val
        else:
            self.data_arr[index] = val

    def __len__(self):
        return self.n

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __iter__(self):
        for i in range(self.n):
            yield self.data_arr[i]

    def __repr__(self):
        submit = "["
        for i in range(self.n):
            submit += str(self.data_arr[i])
            if i != self.n - 1:
                submit += ", "
        submit += "]"
        return submit

    def __add__(self, other):
        new_list = ArrayList()
        for elem in self:
            new_list.append(elem)
        for elem in other:
            new_list.append(elem)
        return new_list

    def __iadd__(self, other):
        for elem in other:
            self.append(elem)
        return self

    def __mul__(self, val):
        new_arr = ArrayList()
        for i in range(val):
            new_arr += self
        return new_arr

    def __rmul__(self, val):
        new_arr = ArrayList()
        for i in range(val):
            new_arr += self
        return new_arr

    def insert(self, index, val):
        if not -self.n <= index <= self.n - 1:
            raise IndexError("invalid index")
        self.append(0)
        if index >= 0:
            rounds = len(self) - index - 1
        else:
            rounds = -index - 1
        for i in range(rounds):
            self[-i - 1] = self[-i - 2]
        self[index] = val

    def pop(self, index=-1):
        if self.n == 0:
            raise IndexError("no element in list")
        if not -self.n <= index <= self.n - 1:
            raise IndexError("invalid index")
        return_value = self[index]
        if index < 0:
            index = self.n + index
        for i in range(index, self.n - 1):
            self[i] = self[i + 1]
        self.n -= 1
        if self.n < self.capacity // 4:
            self.resize(self.capacity // 2)
        return return_value
