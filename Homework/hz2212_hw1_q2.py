def shift(lst, k, dir="left"):
    if dir == "left":
        tmp = lst[:k]
        for i in range(k, len(lst)):
            lst[i - k] = lst[i]
        for i in range(len(tmp)):
            lst[len(lst) - k + i] = tmp[i]
    else:
        tmp = lst[-k:]
        for i in range(len(lst) - k):
            lst[len(lst) - i - 1] = lst[len(lst) - i - k - 1]
        for i in range(len(tmp)):
            lst[i] = tmp[i]
    return lst
