import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(node1, node2, srt_lnk_lst1, srt_lnk_lst2):
        if node1.data is None and node2.data is not None:
            new_lst = DoublyLinkedList()
            while node2.data is not None:
                new_lst.add_last(node2.data)
                node2 = node2.next
        elif node1.data is not None and node2.data is None:
            new_lst = DoublyLinkedList()
            while node1.data is not None:
                new_lst.add_last(node1.data)
                node1 = node1.next
        else:
            if node1.data > node2.data:
                new_lst = merge_sublists(
                    node1, node2.next, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(node2.data)
            else:
                new_lst = merge_sublists(
                    node1.next, node2, srt_lnk_lst1, srt_lnk_lst2)
                new_lst.add_first(node1.data)
        return new_lst

    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, srt_lnk_lst1, srt_lnk_lst2)
