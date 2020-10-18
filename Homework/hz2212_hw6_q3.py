import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        count = 1
        for i in range(1, len(orig_str)):
            if orig_str[i] == orig_str[i - 1]:
                count += 1
            else:
                self.data.add_last((orig_str[i - 1], count))
                count = 1
        if len(orig_str) != 0:
            self.data.add_last((orig_str[len(orig_str) - 1], count))

    def __add__(self, other):
        new_compstr = CompactString("")
        cursor = self.data.header.next
        while cursor.next.data is not None:
            new_compstr.data.add_last(cursor.data)
            cursor = cursor.next
        if cursor.data[0] == other.data.header.next.data[0]:
            new_compstr.data.add_last(
                (cursor.data[0], cursor.data[1] + other.data.header.next.data[1]))
            cursor = other.data.header.next.next
        else:
            new_compstr.data.add_last(cursor.data)
            cursor = other.data.header.next
        while cursor.data is not None:
            new_compstr.data.add_last(cursor.data)
            cursor = cursor.next
        return new_compstr

    def __lt__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return False
        elif cursor1.data is None and cursor2.data is not None:
            return True
        elif cursor1.data is not None and cursor2.data is None:
            return False
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return False
                    return cursor1.data[0] < cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return True
                    return cursor1.next.data[0] < cursor2.data[0]
            return cursor1.data[0] < cursor2.data[0]

    def __le__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return True
        elif cursor1.data is None and cursor2.data is not None:
            return True
        elif cursor1.data is not None and cursor2.data is None:
            return False
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return False
                    return cursor1.data[0] < cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return True
                    return cursor1.next.data[0] < cursor2.data[0]
            return cursor1.data[0] < cursor2.data[0]

    def __gt__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return False
        elif cursor1.data is None and cursor2.data is not None:
            return False
        elif cursor1.data is not None and cursor2.data is None:
            return True
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return True
                    return cursor1.data[0] > cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return False
                    return cursor1.next.data[0] > cursor2.data[0]
            return cursor1.data[0] > cursor2.data[0]

    def __ge__(self, other):
        cursor1 = self.data.header.next
        cursor2 = other.data.header.next
        while cursor1.data == cursor2.data and cursor1.data is not None:
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1.data is None and cursor2.data is None:
            return True
        elif cursor1.data is None and cursor2.data is not None:
            return False
        elif cursor1.data is not None and cursor2.data is None:
            return True
        else:
            if cursor1.data[0] == cursor2.data[0]:
                if cursor1.data[1] > cursor2.data[1]:
                    if cursor2.next.data is None:
                        return True
                    return cursor1.data[0] > cursor2.next.data[0]
                else:
                    if cursor1.next.data is None:
                        return False
                    return cursor1.next.data[0] > cursor2.data[0]
            return cursor1.data[0] > cursor2.data[0]

    def __repr__(self):
        cursor = self.data.header.next
        str = ""
        while cursor.data is not None:
            str += cursor.data[0] * cursor.data[1]
            cursor = cursor.next
        return str
