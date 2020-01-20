def find_min_abs_difference(bst):
    # return tuple containing min, max and find_min_abs_difference
    def find_min_abs_difference_helper(node):
        if node.left is None and node.right is None:
            return (node.item.key, node.item.key, None)
        else:
            if node.left is None and node.right is not None:
                right_tup = find_min_abs_difference_helper(node.right)
                minimum = node.item.key
                maximum = right_tup[1]
                min_diff_tup = (right_tup[0] - node.item.key, right_tup[2])
            elif node.left is not None and node.right is None:
                left_tup = find_min_abs_difference_helper(node.left)
                minimum = left_tup[0]
                maximum = node.item.key
                min_diff_tup = (node.item.key - left_tup[1], left_tup[2])
            else:
                left_tup = find_min_abs_difference_helper(node.left)
                right_tup = find_min_abs_difference_helper(node.right)
                minimum = left_tup[0]
                maximum = right_tup[1]
                min_diff_tup = (
                    node.item.key - left_tup[1], right_tup[0] - node.item.key, left_tup[2], right_tup[2])
            return (minimum, maximum, min(val for val in min_diff_tup if val is not None))
    if bst.root is None:
        raise Exception("min_abs_diff not defined on an empty tree")
    if bst.root.left is None and bst.root.right is None:
        raise Exception("min_abs_diff not defined on a tree with single node")
    return find_min_abs_difference_helper(bst.root)[2]
