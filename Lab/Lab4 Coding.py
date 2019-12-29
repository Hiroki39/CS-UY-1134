def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        (lst[i], lst[n - i - 1]) = (lst[n - i - 1], lst[i])


def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


def move_zeroes(nums):
    count = 0
    index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0


def find_missing(lst):
    for i in range(len(lst)):
        if i != lst[i]:
            return i
    return len(lst)


def find_missing2(lst):
    status_list = [1 for i in range(len(lst) + 1)]
    for i in range(len(lst)):
        status_list[lst[i]] = 0
    for i in range(len(status_list)):
        if status_list[i] == 1:
            return i
