def min_max_BST(bst):
    if bst.root is None:
        raise Exception("min and max not defined on an empty BST")
    cursor1 = bst.root
    cursor2 = bst.root
    while cursor1.left is not None:
        cursor1 = cursor1.left
    while cursor2.right is not None:
        cursor2 = cursor2.right
    return (cursor1.item.key, cursor2.item.key)


def glt_n(bst, n):
    curr_num = None
    find = bst.root
    while find is not None:
        if find.item.key < n:
            if find is bst.root:
                curr_num = find
            find = find.right
        elif find.item.key > n:
            find = find.left
        else:
            return find.item.key
        if find is not None and find.item.key < n:
            curr_num = find
    if curr_num is None:
        return -1
    return curr_num.item.key


def compare_BST(bst1, bst2):
    if len(bst1) != len(bst2):
        return False
    for i, j in zip(bst1, bst2):
        if i != j:
            return False
    return True


def is_BST(root):
    def is_BST_helper(root):
        if root.left is None and root.right is None:
            return (root.item.key, root.item.key, True)
        elif root.left is not None and root.right is None:
            left_tup = is_BST_helper(root.left)
            if root.item.key > left_tup[1] and left_tup[2]:
                return (left_tup[0], root.item.key, True)
            return (left_tup[0], root.item.key, False)
        elif root.left is None and root.right is not None:
            right_tup = is_BST_helper(root.right)
            if root.item.key < right_tup[0] and right_tup[2]:
                return (root.item.key, right_tup[1], True)
            return (root.item.key, right_tup[1], False)
        else:
            left_tup = is_BST_helper(root.left)
            right_tup = is_BST_helper(root.right)
            if left_tup[1] < root.item.key < right_tup[0] and left_tup[2] and right_tup[2]:
                return (left_tup[0], right_tup[1], True)
            return (left_tup[0], right_tup[1], False)
    if root is None:
        raise Exception("tree is empty")
    return is_BST_helper(root)[2]


def lca_BST(bst, node1, node2):
    cursor = bst.root
    while not (node1.item.key <= cursor.item.key <= node2.item.key or node2.item.key <= cursor.item.key <= node1.item.key):
        if cursor.item.key >= node1.item.key and cursor.item.key >= node2.item.key:
            cursor = cursor.left
        else:
            cursor = cursor.right
    return cursor


def lca_BT(bst, node1, node2):
    depth_1 = 0
    depth_2 = 0
    depth_cursor = node1
    while depth_cursor is not bst.root:
        depth_cursor = depth_cursor.parent
        depth_1 += 1
    depth_cursor = node2
    while depth_cursor is not bst.root:
        depth_cursor = depth_cursor.parent
        depth_2 += 1
    if depth_1 < depth_2:
        for i in range(depth_2 - depth_1):
            node2 = node2.parent
    elif depth_1 > depth_2:
        for i in range(depth_1 - depth_2):
            node1 = node1.parent
    while node1 is not node2:
        node1 = node1.parent
        node2 = node2.parent
    return node1
