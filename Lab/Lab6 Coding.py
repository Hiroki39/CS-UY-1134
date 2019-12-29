import os


def sum_to(n):
    if n == 0:
        return 0
    return n + sum_to(n - 1)


def product_even(n):
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n % 2 == 0:
        return n * product_even(n - 2)
    return product_even(n - 1)


def find_max(lst, low, high):
    if low == high:
        return lst[low]
    if lst[low] > find_max(lst, low + 1, high):
        return lst[low]
    return find_max(lst, low + 1, high)


def is_palindrome(input_str, low, high):
    if high - low <= 1:
        if input_str[low] == input_str[high]:
            return True
        return False
    else:
        if input_str[low] == input_str[high]:
            return is_palindrome(input_str, low + 1, high - 1)
        return False


def binary_search(lst, low, high, val):
    mid = (low + high) // 2
    if low > high:
        return None
    if lst[mid] == val:
        return mid
    elif lst[mid] < val:
        return binary_search(lst, mid + 1, high, val)
    else:
        return binary_search(lst, low, mid, val)


def split_parity(lst, low, high):
    if low < high:
        if lst[low] % 2 == 0:
            split_parity(lst, low + 1, high)
        elif lst[high] % 2 != 0:
            split_parity(lst, low, high - 1)
        else:
            (lst[low], lst[high]) = (lst[high], lst[low])
            split_parity(lst, low + 1, high - 1)


def vc_count(word, low, high):
    if low == high:
        return (1, 0) if word[low] in ['a', 'e', 'i', 'o', 'u',
                                       'A', 'E', 'I', 'O', 'U'] else (0, 1)
    return(vc_count(word, low, low)[0] + vc_count(word, low + 1, high)[0],
           vc_count(word, low, low)[1] + vc_count(word, low + 1, high)[1])


def nested_sum(lst):
    return lst if isinstance(lst, int) else \
        sum([nested_sum(elem) for elem in lst])


def disk_usage(path):
    return os.path.getsize(path) if not os.path.isdir(path) else \
        sum([disk_usage(os.path.join(path, file_and_dir)) for
             file_and_dir in os.listdir(path)]) + os.path.getsize(path)
