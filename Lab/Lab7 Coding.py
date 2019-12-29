def str_to_int(int_str):
    num = 0
    for i in range(len(int_str)):
        num += int(int_str[i]) * 10 ** (len(int_str) - i - 1)
    return num


def two_max_product(lst):
    max1 = lst[0]
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > max1:
            max1 = lst[i]
            max_index = i
    lst.pop(max_index)
    max2 = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max2:
            max2 = lst[i]
    return max1 * max2


def non_vowels(input_str, low, high):
    if low == high:
        if input_str[low] in ['a', 'e', 'i', 'o', 'u',
                              'A', 'E', 'I', 'O', 'U']:
            return []
        return [input_str[low]]
    return non_vowels(input_str, low, low) + \
        non_vowels(input_str, low + 1, high)


def find_max_even(lst, low, high):
    if low == high:
        if lst[low] % 2 == 0:
            return lst[low]
        return None
    if find_max_even(lst, low, low) and find_max_even(lst, low + 1, high):
        return max(find_max_even(lst, low, low),
                   find_max_even(lst, low + 1, high))
    elif find_max_even(lst, low, low) is None and \
            find_max_even(lst, low + 1, high) is not None:
        return find_max_even(lst, low + 1, high)
    elif find_max_even(lst, low, low) is not None and \
            find_max_even(lst, low + 1, high) is None:
        return find_max_even(lst, low, low)
    else:
        return None


def reverse_vowels(input_str):
    def reverse_vowels_helper(input_str, low, high):
        if low < high:
            if input_str[low] not in ['a', 'e', 'i', 'o', 'u',
                                      'A', 'E', 'I', 'O', 'U']:
                reverse_vowels_helper(input_str, low + 1, high)
            elif input_str[high] not in ['a', 'e', 'i', 'o', 'u',
                                         'A', 'E', 'I', 'O', 'U']:
                reverse_vowels_helper(input_str, low, high - 1)
            else:
                (input_str[low], input_str[high]) = \
                    (input_str[high], input_str[low])
                reverse_vowels_helper(input_str, low + 1, high - 1)
        return input_str
    input_str = list(input_str)
    return "".join(reverse_vowels_helper(input_str, 0, len(input_str) - 1))


def square_root(num):
    def square_root_helper(num, low, high):
        if high - low > 0.01:
            mid = (low + high) / 2
            if mid * mid > num:
                return square_root_helper(num, low, mid)
            return square_root_helper(num, mid, high)
        return (low + high) / 2
    return format(square_root_helper(num, 0, num), '0.2f')


def jump_search(lst, val):
    index = 0
    k = round(len(lst) ** 0.5)
    while(index < len(lst) - 1 and lst[index] <= val):
        if lst[index] == val:
            return index
        index += k
    for i in range(index - k + 1, index):
        if i == len(lst) or i <= 0:
            return None
        if lst[i] == val:
            return i
    return None
