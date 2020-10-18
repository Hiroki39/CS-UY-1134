def max_in_linked_list(lnk_lst):
    def max_in_linked_list_helper(lnk_lst, sublist_head):
        if sublist_head.next is lnk_lst.trailer:
            return sublist_head.data
        rest_max = max_in_linked_list_helper(lnk_lst, sublist_head.next)
        return max(sublist_head.data, rest_max)

    if lnk_lst.is_empty():
        raise Exception("List is Empty")
    return max_in_linked_list_helper(lnk_lst, lnk_lst.header.next)
