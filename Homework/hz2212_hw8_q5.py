class BinarySearchTreeMap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):  # keep track of number of nodes on left & right
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.left_num = 0  # attribute for get_ith_smallest
            self.right_num = 0  # attribute for get_ith_smallest

        def num_children(self):
            count = 0
            if self.left is not None:
                count += 1
            if self.right is not None:
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None
            self.left_num = None
            self.right_num = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        node = self.find(key)
        if node is None:
            raise KeyError(str(key) + " not found")
        return node.item.value

    def find(self, key):
        curr = self.root
        while curr is not None:
            if curr.item.key == key:
                return curr
            elif curr.item.key > key:
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None

    def __setitem__(self, key, value):
        node = self.find(key)
        if node is None:
            self.insert(key, value)
        else:
            node.item.value = value

    # assume key not in tree, update left_num or right_num of some nodes during the insert process
    def insert(self, key, value=None):
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

    # update left_num or right_num of some nodes during the delete process
    def delete(self, node_to_delete):
        item = node_to_delete.item
        num_children = node_to_delete.num_children()
        if node_to_delete is self.root:
            if num_children == 0:
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 1:
                if self.root.left is not None:
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1
            else:
                left_max = self.subtree_max(node_to_delete.left)
                node_to_delete.item = left_max.item
                self.delete_node(left_max)
        else:
            if num_children == 0:
                parent = node_to_delete.parent
                if node_to_delete is parent.left:
                    parent.left = None
                    parent.left_num = 0
                else:
                    parent.right = None
                    parent.right_num = 0
                node_to_delete.disconnect()
                self.size -= 1
            elif num_children == 1:
                parent = node_to_delete.parent
                if node_to_delete.left is not None:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right
                child.parent = parent
                if node_to_delete is parent.left:
                    parent.left = child
                    parent.left_num -= 1
                else:
                    parent.right = child
                    parent.right_num -= 1
                node_to_delete.disconnect()
                self.size -= 1
            else:
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.delete_node(max_of_left)
        return item

    def subtree_max(self, curr_root):  # assumes non empty subtree
        node = curr_root
        while node.right is not None:
            node = node.right
        return node

    def inorder(self):
        def subtree_inorder(root):
            if root is None:
                return
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)
        yield from subtree_inorder(self.root)

    def __iter__(self):
        for node in self.inorder():
            yield node.item.key

# Homework8
    def get_ith_smallest(self, i):  # find key by keep track of the current rank
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
