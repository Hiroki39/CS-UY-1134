def binary_search(srt_lst, val):
    left = 0
    right = len(srt_lst) - 1
    mid = (left + right) // 2
    while(val != srt_lst[mid]):
        if(right < left):
            return None
        if(val < srt_lst[mid]):
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid
