def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    while srt_lst[left] + srt_lst[right] != target:
        if srt_lst[left] + srt_lst[right] > target:
            right -= 1
        else:
            left += 1
        if left == right:
            return None
    return (left, right)
