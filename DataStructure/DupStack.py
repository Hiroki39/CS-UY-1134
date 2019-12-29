from ArrayStack import ArrayStack


class DupStack:
    def __init__(self):
        self.data = ArrayStack()
        self.len = 0

    def __len__(self):
        return self.len

    def is_empty(self):
        return self.len == 0

    def push(self, e):
        if self.is_empty():
            self.data.push((e, 1))
        else:
            if self.top() == e:
                count = self.top_dups_count() + 1
                self.data.push((self.data.pop()[0], count))
            else:
                self.data.push((e, 1))
        self.len += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.top()[0]

    def top_dups_count(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        return self.data.top()[1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        tmp_tup = self.data.pop()
        val = tmp_tup[1] - 1
        self.len -= 1
        if val != 0:
            self.data.push((tmp_tup[0], val))
        return tmp_tup[0]

    def pop_dups(self):
        if self.is_empty():
            raise Exception("Stack is Empty")
        tmp_tup = self.data.pop()
        self.len -= tmp_tup[1]
        return tmp_tup[0]
