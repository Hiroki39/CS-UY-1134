import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in range(len(num_str)):
            self.data.add_last(int(num_str[i]))
        while self.data.header.next.data == 0 and len(self.data) > 1:
            self.data.delete_first()

    def __add__(self, other):
        new_num = Integer("")
        cursor1 = self.data.trailer.prev
        cursor2 = other.data.trailer.prev
        carry = 0
        while cursor1.data is not None and cursor2.data is not None:
            result = cursor1.data + cursor2.data + carry
            new_num.data.add_first(result % 10)
            carry = result // 10
            cursor1 = cursor1.prev
            cursor2 = cursor2.prev
        if cursor1.data is not None:
            long_cursor = cursor1
        else:
            long_cursor = cursor2
        while long_cursor.data is not None:
            new_num.data.add_first((long_cursor.data + carry) % 10)
            carry = (long_cursor.data + carry) // 10
            long_cursor = long_cursor.prev
        if carry != 0:
            new_num.data.add_first(carry)
        return new_num

    def __repr__(self):
        cursor = self.data.header.next
        num_str = ""
        while cursor.data is not None:
            num_str += str(cursor.data)
            cursor = cursor.next
        return num_str

    def __mul__(self, other):
        new_num = Integer("")
        cursor1 = self.data.trailer.prev
        for i in range(len(self.data)):
            cursor2 = other.data.trailer.prev
            carry = 0
            tmp_num = Integer("")
            for j in range(len(other.data)):
                result = cursor1.data * cursor2.data + carry
                tmp_num.data.add_first(result % 10)
                carry = result // 10
                cursor2 = cursor2.prev
            if carry != 0:
                tmp_num.data.add_first(carry)
            for j in range(i):
                tmp_num.data.add_last(0)
            new_num = new_num + tmp_num
            cursor1 = cursor1.prev
        while new_num.data.header.next.data == 0 and len(new_num.data) > 1:
            new_num.data.delete_first()
        return new_num
