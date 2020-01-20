from ArrayList import ArrayList


class ArrayHeap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.data_arr = ArrayList()

    def __len__(self):
        return len(self.data_arr)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value=None):
        new_item = ArrayHeap.Item(key, value)
        self.data_arr.append(new_item)
        self.upward_min_heapify(len(self) - 1)

    def upward_min_heapify(self, index):  # restore attributes of heap
        while index != 0 and self.data_arr[index].key < self.data_arr[(index - 1) // 2].key:
            self.data_arr[index], self.data_arr[(
                index - 1) // 2] = self.data_arr[(index - 1) // 2], self.data_arr[index]
            index = (index - 1) // 2

    def min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.data_arr[0].key, self.data_arr[0].value

    def remove_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        item = self.data_arr[0]
        if len(self) != 1:
            self.data_arr[0] = self.data_arr.pop()
        else:
            self.data_arr.pop()
        self.downward_min_heapify(0)
        return item.key, item.value

    def downward_min_heapify(self, index):  # restore attributes of heap
        while index * 2 + 1 < len(self):
            if self.data_arr[index].key > self.data_arr[index * 2 + 1].key:
                if index * 2 + 2 >= len(self) or self.data_arr[index * 2 + 2].key > self.data_arr[index * 2 + 1].key:
                    index = index * 2 + 1
                else:
                    index = index * 2 + 2
            else:
                if index * 2 + 2 < len(self) and self.data_arr[index].key > self.data_arr[index * 2 + 2].key:
                    index = index * 2 + 2
                else:
                    break
            self.data_arr[index], self.data_arr[(
                index - 1) // 2] = self.data_arr[(index - 1) // 2], self.data_arr[index]
