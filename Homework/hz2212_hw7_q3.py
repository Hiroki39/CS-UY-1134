def is_height_balanced(bin_tree):
    def is_subtree_height_balanced(root):
        if root is None:
            return (True, 0)
        left_tup = is_subtree_height_balanced(root.left)
        right_tup = is_subtree_height_balanced(root.right)
        height = max(left_tup[1], right_tup[1]) + 1
        if not (left_tup[0] and right_tup[0]) or abs(left_tup[1] - right_tup[1]) > 1:
            return (False, height)
        return (True, height)
    if bin_tree.root is None:
        raise Exception("height-balance propertie not defined on empty tree")
    return is_subtree_height_balanced(bin_tree.root)[0]
