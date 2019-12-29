def find_duplicates(lst):
    duplicates = []
    count_lst = [0 for i in range(len(lst) - 1)]
    for i in range(len(lst)):
        count_lst[lst[i] - 1] += 1
    for i in range(len(count_lst)):
        if count_lst[i] > 1:
            duplicates.append(i + 1)
    return duplicates
