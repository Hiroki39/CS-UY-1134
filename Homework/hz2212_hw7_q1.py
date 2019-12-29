class EmptyTree(Exception):
    pass


def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        elif root.left is None and root.right is not None:
            right_tup = subtree_min_and_max(root.right)
            return (min(right_tup[0], root.data), max(right_tup[1], root.data))
        elif root.left is not None and root.right is None:
            left_tup = subtree_min_and_max(root.left)
            return (min(left_tup[0], root.data), max(left_tup[1], root.data))
        else:
            left_tup = subtree_min_and_max(root.left)
            right_tup = subtree_min_and_max(root.right)
            return (min(left_tup[0], right_tup[0], root.data), max(left_tup[1], right_tup[1], root.data))
    if bin_tree.root is None:
        raise EmptyTree("min and max not defined on empty tree")
    return subtree_min_and_max(bin_tree.root)
