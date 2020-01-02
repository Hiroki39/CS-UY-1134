import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from BinaryTreeHeap import BinaryTreeHeap


def heap_sort(lst):
    helper_heap = BinaryTreeHeap()
    for elem in lst:
        helper_heap.add(elem)
    for i in range(len(helper_heap)):
        lst[i] = helper_heap.remove_min()[0]
