def merge_sort(lst):
    def merge_sort_helper(lst, low, high):
        if low != high:
            mid = (low + high) // 2
            merge_sort_helper(lst, low, mid)
            merge_sort_helper(lst, mid + 1, high)
            merge(lst, low, mid, high)

    def merge(lst, low_left, high_left, high_right):
        low_right = high_left + 1
        merged_list = []
        ind1 = low_left
        ind2 = low_right
        while ind1 <= high_left and ind2 <= high_right:
            if lst[ind1] < lst[ind2]:
                merged_list.append(lst[ind1])
                ind1 += 1
            else:
                merged_list.append(lst[ind2])
                ind2 += 1
        while ind1 <= high_left:
            merged_list.append(lst[ind1])
            ind1 += 1
        while ind2 <= high_right:
            merged_list.append(lst[ind2])
            ind2 += 1
        for i in range(len(merged_list)):
            lst[low_left + i] = merged_list[i]

    if len(lst) != 0:
        merge_sort_helper(lst, 0, len(lst) - 1)
