def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    new_lst = []
    for i in range(high - low + 1):
        for sublst in permutations(lst, low + 1, high):
            sublst.insert(i, lst[low])
            new_lst.append(sublst)
    return new_lst
