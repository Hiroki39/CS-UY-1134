class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.left_num = 0  # attribute for hw8
            self.right_num = 0  # attribute for hw8
            self.parent = None

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.left_num = None
            self.right_num = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):  # return the value associated with key
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        return node.item.value

    def find(self, key):
        curr_node = self.root
        while curr_node is not None:
            if key < curr_node.item.key:
                curr_node = curr_node.left
            elif key > curr_node.item.key:
                curr_node = curr_node.right
            else:
                return curr_node
        return None

    def __setitem__(self, key, value):
        node = self.find(key)
        if node is not None:
            node.item.value = value
        else:
            self.insert(key, value)

    def insert(self, key, value=None):  # assume key not in tree
        new_item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(new_item)
        parent = None
        curr_node = self.root
        if curr_node is None:
            self.root = new_node
        else:
            while curr_node is not None:
                parent = curr_node
                if curr_node.item.key > key:
                    curr_node.left_num += 1
                    curr_node = curr_node.left
                else:
                    curr_node.right_num += 1
                    curr_node = curr_node.right
            if key < parent.item.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
        self.size += 1

    def __delitem__(self, key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        else:
            self.delete(node)

    def delete(self, node_to_delete):  # assume key is in the tree
        item = node_to_delete.item
        parent = node_to_delete.parent
        # replace the content of the node with the content of the node with the largest key in the left tree
        if node_to_delete.left is not None and node_to_delete.right is not None:
            max_in_left = self.subtree_max(node_to_delete.left)
            node_to_delete.item = max_in_left.item
            self.delete(max_in_left)
        else:
            if node_to_delete.left is None and node_to_delete.right is None:
                child = None
            elif node_to_delete.left is not None and node_to_delete.right is None:
                child = node_to_delete.left
            else:
                child = node_to_delete.right
            if parent is None:
                self.root = child
            else:
                if parent.left is node_to_delete:
                    parent.left = child
                    parent.left_num -= 1
                else:
                    parent.right = child
                    parent.right_num -= 1
                curr_node = parent
                while curr_node.parent is not None:
                    if curr_node is curr_node.parent.left:
                        curr_node.parent.left_num -= 1
                    else:
                        curr_node.parent.right_num -= 1
                    curr_node = curr_node.parent
            if child is not None:
                child.parent = parent
            node_to_delete.disconnect()
            self.size -= 1
        return item  # returns item in the node that is removed

    def subtree_max(self, subtree_root):
        curr = subtree_root
        while curr.right is not None:
            curr = curr.right
        return curr

    def inorder(self):  # yield references
        def subtree_inorder(root):
            if root is None:
                return
            yield from subtree_inorder(root.left)
            yield root
            yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

    def __iter__(self):  # yield keys
        for node in self.inorder():
            yield node.item.key

# Homework8
    def get_ith_smallest(self, i):
        if not 1 <= i <= self.size:
            raise IndexError()
        curr = self.root
        curr_rank = self.root.left_num + 1
        while i != curr_rank:
            if i > curr_rank:
                curr = curr.right
                curr_rank += curr.left_num + 1
            else:
                curr = curr.left
                curr_rank -= curr.right_num + 1
        return curr.item.key
