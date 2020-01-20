from SinglyLinkedList import SinglyLinkedList
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def reverse_dll_by_data(dll):
    cursor1 = dll.header.next
    cursor2 = dll.trailer.prev
    for i in range(len(dll) // 2):
        cursor1.data, cursor2.data = cursor2.data, cursor1.data
        cursor1 = cursor1.next
        cursor2 = cursor2.prev


def reverse_dll_by_node(dll):
    cursor = dll.header
    while cursor is not None:
        cursor.next, cursor.prev = cursor.prev, cursor.next
        cursor = cursor.prev
    dll.header, dll.trailer = dll.trailer, dll.header


class Integer:
    def __init__(self, num_str):
        self.data = SinglyLinkedList()
        for i in range(len(num_str)):
            self.data.add_first(int(num_str[i]))

    def __iadd__(self, other):
        cursor1 = self.data.header
        cursor2 = other.data.header
        carry = 0
        while cursor2.next is not None:
            result = cursor1.next.data + cursor2.next.data + carry
            cursor1.next.data = result % 10
            carry = result // 10
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        while cursor1.next is not None:
            result = cursor1.next.data + carry
            cursor1.next.data = result % 10
            carry = result // 10
            cursor1 = cursor1.next
        if carry != 0:
            self.data.add_after(cursor1, carry)
        return self

    def __repr__(self):
        cursor = self.data.header
        num_str = ""
        while cursor.next is not None:
            num_str = str(cursor.next.data) + num_str
            cursor = cursor.next
        return num_str
