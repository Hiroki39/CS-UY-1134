class AVLFlipTreeMap:
    class Item:
        def __init__(self, key, value=None, flip=False):
            self.key = key
            self.value = value
            self.flip = flip

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.height = 0
            self.parent = None

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.height = None
            self.parent = None

        def get_diff(self):
            if self.left is not None:
                left = self.left.height
            else:
                left = -1
            if self.right is not None:
                right = self.right.height
            else:
                right = -1
            return right - left

        def set_height(self):
            if self.left is None and self.right is None:
                self.height = 0
            elif self.left is not None and self.right is None:
                self.height = self.left.height + 1
            elif self.left is None and self.right is not None:
                self.height = self.right.height + 1
            else:
                self.height = max(self.left.height, self.right.height) + 1

        def check_flip(self):
            flipped = False
            node = self
            while node is not None:
                flipped ^= node.item.flip
                node = node.parent
            return flipped

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
            return -1
        if node.check_flip():
            return -node.item.value
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
            if node.check_flip():
                node.item.value = -value
            else:
                node.item.value = value
        else:
            self.insert(key, value)

    def insert(self, key, value=None, flip=False):  # assume key not in tree
        new_item = AVLFlipTreeMap.Item(key, value, flip)
        new_node = AVLFlipTreeMap.Node(new_item)
        parent = None
        curr_node = self.root
        if curr_node is None:
            self.root = new_node
        else:
            while curr_node is not None:
                parent = curr_node
                if curr_node.item.key > key:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            if key < parent.item.key:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            if new_node.check_flip():
                new_node.item.value *= -1
            self.fix_avl_property(new_node.parent)
        self.size += 1

    def fix_avl_property(self, node):
        while node is not None:
            node.set_height()
            if abs(node.get_diff()) > 1:
                node = self.rotate(node)
            node = node.parent

    def rotate(self, node):
        if node.get_diff() > 0:
            if node.right.get_diff() == -1:
                self.rotate(node.right)

            new_root = node.right
            self.pushdown(node)
            self.pushdown(new_root)

            node.right = new_root.left
            if new_root.left is not None:
                new_root.left.parent = node
            new_root.left = node
        else:
            if node.left.get_diff() == 1:
                self.rotate(node.left)

            new_root = node.left
            self.pushdown(node)
            self.pushdown(new_root)

            node.left = new_root.right
            if new_root.right is not None:
                new_root.right.parent = node
            new_root.right = node

        node.set_height()
        new_root.set_height()
        new_root.parent = node.parent
        node.parent = new_root

        if new_root.parent is not None:
            if new_root.parent.left is node:
                new_root.parent.left = new_root
            else:
                new_root.parent.right = new_root
        else:
            self.root = new_root
        return new_root

    def pushdown(self, node):  # make sure the node involved in the rotation is not flipped
        if node.item.flip:
            node.item.flip = False
            node.item.value *= -1
            if node.left is not None:
                node.left.item.flip ^= True
            if node.right is not None:
                node.right.item.flip ^= True

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

            if max_in_left.check_flip() == node_to_delete.check_flip():
                node_to_delete.item.key = max_in_left.item.key
                node_to_delete.item.value = max_in_left.item.value
            else:
                node_to_delete.item.key = max_in_left.item.key
                node_to_delete.item.value = -max_in_left.item.value

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
                else:
                    parent.right = child
            if child is not None:
                if node_to_delete.item.flip:
                    child.item.flip ^= True
                child.parent = parent
            node_to_delete.disconnect()
            self.fix_avl_property(parent)
            self.size -= 1
        return item  # returns item in the node that is removed

    def subtree_max(self, subtree_root):
        curr = subtree_root
        while curr.right is not None:
            curr = curr.right
        return curr

    def flip(self, low, high):
        if high < low:
            low, high = high, low

        if self.root is None:
            return

        subtree_root = self.root
        while not low <= subtree_root.item.key <= high:
            if subtree_root.item.key < low:
                subtree_root = subtree_root.right
            else:
                subtree_root = subtree_root.left
            if subtree_root is None:
                return

        subtree_root.item.value *= -1

        if subtree_root.item.key != low:
            low_cursor = subtree_root.left
            while low_cursor is not None and low_cursor.item.key != low:
                if low_cursor.item.key > low:
                    if low_cursor.right is not None:
                        low_cursor.right.item.flip ^= True
                    low_cursor.item.value *= -1
                    low_cursor = low_cursor.left
                else:
                    low_cursor = low_cursor.right

            if low_cursor is not None:
                if low_cursor.right is not None:
                    low_cursor.right.item.flip ^= True
                low_cursor.item.value *= -1

        if subtree_root.item.key != high:
            high_cursor = subtree_root.right
            while high_cursor is not None and high_cursor.item.key != high:
                if high_cursor.item.key < high:
                    if high_cursor.left is not None:
                        high_cursor.left.item.flip ^= True
                    high_cursor.item.value *= -1
                    high_cursor = high_cursor.right
                else:
                    high_cursor = high_cursor.left

            if high_cursor is not None:
                if high_cursor.left is not None:
                    high_cursor.left.item.flip ^= True
                high_cursor.item.value *= -1

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
