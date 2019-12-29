from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


class LinkedBinaryTree:
    class Node:
        def __init__(self, data=None, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.parent = None
            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def count_nodes(self, root):
        def subtree_count_nodes(root):
            if root is None:
                return 0
            left_count = subtree_count_nodes(root.left)
            right_count = subtree_count_nodes(root.right)
            return left_count + right_count + 1
        return subtree_count_nodes(self.root)

    def sum(self):
        def subtree_sum(root):
            if root is None:
                return 0
            left_sum = subtree_sum(root.left)
            right_sum = subtree_sum(root.right)
            return left_sum + right_sum + root.data
        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if root is None:
                return -1
            left_height = subtree_height(root.left)
            right_height = subtree_height(root.right)
            return max(left_height, right_height) + 1
        if self.root is None:
            raise Exception("Height not defined on empty tree")
        return subtree_height(self.root)

    def preorder(self):  # yield references
        def subtree_preorder(root):
            if root is None:
                return
            yield root
            yield from subtree_preorder(root.left)
            yield from subtree_preorder(root.right)
        yield from subtree_preorder(self.root)

    def inorder(self):  # yield references
        def subtree_inorder(root):
            if root is None:
                return
            yield from subtree_inorder(root.left)
            yield root
            yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

    def postorder(self):  # yield references
        def subtree_postorder(root):
            if root is None:
                return
            yield from subtree_postorder(root.left)
            yield from subtree_postorder(root.right)
            yield root
        yield from subtree_postorder(self.root)

    def breadth_first(self):  # yield references
        if self.root is None:
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while not line.is_empty():
            curr_node = line.dequeue()
            yield curr_node
            if curr_node.left is not None:
                line.enqueue(curr_node.left)
            if curr_node.right is not None:
                line.enqueue(curr_node.right)

    def __iter__(self):  # yield data
        for node in self.inorder():
            yield node.data

# Lab12
    def preorder_with_stack(self):  # yield data
        helper_stack = ArrayStack()
        helper_stack.push(self.root)
        while not helper_stack.is_empty():
            curr_node = helper_stack.pop()
            yield curr_node.data
            if curr_node.right is not None:
                helper_stack.push(curr_node.right)
            if curr_node.left is not None:
                helper_stack.push(curr_node.left)

# Homework7
    def leaves_list(self):
        def leaves_generater(root):
            if root.left is None and root.right is None:
                yield root
            elif root.left is not None and root.right is None:
                yield from leaves_generater(root.left)
            elif root.left is None and root.right is not None:
                yield from leaves_generater(root.right)
            else:
                yield from leaves_generater(root.left)
                yield from leaves_generater(root.right)
        if self.root is None:
            return []
        return [node.data for node in leaves_generater(self.root)]

    def iterative_inorder(self):
        curr_node = self.root
        while curr_node is not None:
            if curr_node.left is None:
                identifier = None
                while curr_node is not None and (curr_node.right is None or curr_node.right is identifier):
                    identifier = curr_node
                    if curr_node.right is None:
                        yield curr_node.data
                    curr_node = curr_node.parent
                if curr_node is not None:
                    yield curr_node.data
                    curr_node = curr_node.right
            else:
                curr_node = curr_node.left
