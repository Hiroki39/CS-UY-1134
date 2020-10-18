import sys
sys.path.append(sys.path[0] + '/../DataStructure')
sys.path.append(sys.path[0] + '/../Algorithm')
from MergeSort import merge_sort
from ChainingHashTableMap import ChainingHashTableMap


def intersection_list1(lst1, lst2):
    merge_sort(lst1)
    merge_sort(lst2)
    ind1 = 0
    ind2 = 0
    int_lst = []
    while ind1 < len(lst1) and ind2 < len(lst2):
        if lst1[ind1] < lst2[ind2]:
            ind1 += 1
        elif lst1[ind1] > lst2[ind2]:
            ind2 += 1
        else:
            int_lst.append(lst1[ind1])
            ind1 += 1
            ind2 += 1
    return int_lst


def intersection_list2(lst1, lst2):
    element_map = ChainingHashTableMap()
    for elem in lst1:
        element_map[elem] = None
    int_lst = []
    for elem in lst2:
        try:
            element_map[elem]
            int_lst.append(elem)
        except KeyError:
            pass
    return int_lst
