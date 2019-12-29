from ArrayList import ArrayList


class UnsortedArrayMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.table = ArrayList()

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return len(self.table) == 0

    def __getitem__(self, key):
        for item in self.table:
            if item.key == key:
                return item.value
        raise KeyError(str(key) + " not found")

    def __setitem__(self, key, value):
        for item in self.table:
            if item.key == key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for i in range(len(self.table)):
            if self.table[i].key == key:
                self.table.pop(i)
                return
        raise KeyError(str(key) + " not found")

    def __iter__(self):
        for item in self.table:
            yield item.key
