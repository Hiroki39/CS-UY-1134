def appearances(s, low, high):
    if low == high:
        return {s[low]: 1}
    dict = appearances(s, low + 1, high)
    if s[low] not in dict:
        dict[s[low]] = 1
        return dict
    dict[s[low]] += 1
    return dict
