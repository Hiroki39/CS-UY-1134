def split_parity(lst):
    first_even = 0
    last_odd = len(lst) - 1
    while lst[first_even] % 2 != 0:
        first_even += 1
    while lst[last_odd] % 2 == 0:
        last_odd -= 1
    while first_even < last_odd:
        (lst[first_even], lst[last_odd]) = (lst[last_odd], lst[first_even])
        while lst[first_even] % 2 != 0:
            first_even += 1
        while lst[last_odd] % 2 == 0:
            last_odd -= 1
