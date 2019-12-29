def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    mid = (left + right) // 2
    while not (lst01[mid] == 1 and lst01[mid - 1] == 0):
        if(lst01[mid] == 1):
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return mid
