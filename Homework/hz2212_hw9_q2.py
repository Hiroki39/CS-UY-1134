import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from ChainingHashTableMap import ChainingHashTableMap


def intersection_list1(lst1, lst2):
    return [elem for elem in lst1 if elem in lst2]


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
