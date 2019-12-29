def list_min(lst, low, high):
    if low == high:
        return lst[low]
    min = list_min(lst, low + 1, high)
    if lst[low] < min:
        return lst[low]
    return min
