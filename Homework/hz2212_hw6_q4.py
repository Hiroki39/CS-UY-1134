import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    copied_lst = DoublyLinkedList()
    for data in lnk_lst:
        copied_lst.add_last(data)
    return copied_lst


def deep_copy_linked_list(lnk_lst):
    copied_lst = DoublyLinkedList()
    for data in lnk_lst:
        if isinstance(data, int):
            copied_lst.add_last(data)
        else:
            copied_lst.add_last(deep_copy_linked_list(data))
    return copied_lst
