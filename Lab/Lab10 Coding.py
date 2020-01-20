from ArrayStack import ArrayStack
from DoublyLinkedList import DoublyLinkedList
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def flatten_dll(lnk_lst):
    def flatten_dll_helper(node, dll):
        while node.data is not None:
            if isinstance(node.data, DoublyLinkedList):
                flatten_dll_helper(node.data.header.next, dll)
            else:
                dll.add_last(node.data)
            node = node.next
    new_dll = DoublyLinkedList()
    flatten_dll_helper(lnk_lst.header.next, new_dll)
    return new_dll


def flatten_dll2(lnk_lst):
    helper_stack = ArrayStack()
    new_dll = DoublyLinkedList()
    while not lnk_lst.is_empty():
        helper_stack.push(lnk_lst.delete_last())
    while not helper_stack.is_empty():
        elem = helper_stack.pop()
        if isinstance(elem, DoublyLinkedList):
            while not elem.is_empty():
                helper_stack.push(elem.delete_last())
        else:
            new_dll.add_last(elem)
    return new_dll
