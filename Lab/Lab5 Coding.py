import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size

    def __getitem__(self, ind):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError("invalid index")
        if (ind < 0):
            return self.data_arr[self.n + ind]
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError("invalid index")
        if (ind < 0):
            self.data_arr[self.n + ind] = val
        else:
            self.data_arr[ind] = val

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
            if (i != self.n - 1):
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
