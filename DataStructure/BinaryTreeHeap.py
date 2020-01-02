class BinaryTreeHeap:
    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None

        def disconnect(self):
            self.item = None
            self.left = None
            self.right = None
            self.parent = None

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value=None):
        new_item = BinaryTreeHeap.Item(key, value)
        new_node = BinaryTreeHeap.Node(new_item)
        parent = self.find_parent(len(self))  # insert node in correct position
        if parent is None:
            self.root = new_node
        elif parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent
        self.upward_min_heapify(new_node)
        self.size += 1

    def find_parent(self, index):
        if index == 0:
            return None
        if (index - 1) // 2 == 0:
            return self.root
        node = self.find_parent((index - 1) // 2)
        if index % 2 == 1:
            return node.left
        return node.right

    def upward_min_heapify(self, node):  # restore attributes of heap
        while node is not self.root and node.item.key < node.parent.item.key:
            node.item, node.parent.item = node.parent.item, node.item
            node = node.parent

    def min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.root.item.key, self.root.item.value

    def remove_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        item = self.root.item
        parent = self.find_parent(len(self) - 1)
        if parent is None:
            node_to_delete = self.root
            self.root = None
        else:
            if parent.right is not None:
                node_to_delete = parent.right
                node_to_delete.parent.right = None
            else:
                node_to_delete = parent.left
                node_to_delete.parent.left = None
            node_to_delete.item, self.root.item = self.root.item, node_to_delete.item
        node_to_delete.disconnect()
        self.downward_min_heapify(self.root)
        self.size -= 1
        return item.key, item.value

    def downward_min_heapify(self, node):  # restore attributes of heap
        while node is not None and node.left is not None:
            if node.item.key > node.left.item.key:
                if node.right is None or node.right.item.key > node.left.item.key:
                    node = node.left
                else:
                    node = node.right
            else:
                if node.right is not None and node.item.key > node.right.item.key:
                    node = node.right
                else:
                    break
            node.item, node.parent.item = node.parent.item, node.item
