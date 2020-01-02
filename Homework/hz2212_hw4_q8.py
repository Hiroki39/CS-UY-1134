def flat_list(nested_lst, low, high):
    if low == high:
        if isinstance(nested_lst[low], int):
            return [nested_lst[low]]
        return flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)
    return flat_list(nested_lst, low, low) + flat_list(nested_lst, low + 1, high)
