from ArrayQueue import ArrayQueue
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def binary_tree_even_sum(root):
    if root is None:
        return 0
    left_sum = binary_tree_even_sum(root.left)
    right_sum = binary_tree_even_sum(root.right)
    if root.data % 2 != 0:
        return left_sum + right_sum
    return left_sum + right_sum + root.data


def binary_tree_has_val(root, val):
    if root is None:
        return False
    if root.data == val:
        return True
    return binary_tree_has_val(root.left, val) or binary_tree_has_val(root.right, val)


def invert_binary_tree1(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invert_binary_tree1(root.left)
    invert_binary_tree2(root.right)


def invert_binary_tree2(root):
    line = ArrayQueue()
    line.enqueue(root)
    while not line.is_empty():
        node = line.dequeue()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            line.enqueue(node.left)
        if node.right is not None:
            line.enqueue(node.right)


def is_full(root):
    if root is None:
        raise Exception("Tree is Empty")
    if root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        return False
    elif root.right is None and root.left is not None:
        return False
    return is_full(root.left) and is_full(root.right)


def is_complete(root):
    line = ArrayQueue()
    line.enqueue(root)
    depth = 0
    while not line.is_empty():
        if len(line) != 2**depth:
            return False
        for i in range(len(line)):
            node = line.dequeue()
            if node.left is not None:
                line.enqueue(node.left)
            if node.right is not None:
                line.enqueue(node.right)
        depth += 1
    return True
