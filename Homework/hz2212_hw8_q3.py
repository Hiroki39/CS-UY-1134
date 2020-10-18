import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    # returns tuples containing the connect position and current node
    def restore_bst_helper(prefix_lst, start_pos, val_to_insert):
        new_item = BinarySearchTreeMap.Item(prefix_lst[start_pos])
        curr_node = BinarySearchTreeMap.Node(
            new_item)  # create subtrees leaning to left
        if start_pos == 0:
            return curr_node, curr_node
        connect_pos = None
        while prefix_lst[start_pos] < prefix_lst[start_pos - 1]:
            start_pos -= 1
            prev_node = curr_node
            new_item = BinarySearchTreeMap.Item(prefix_lst[start_pos])
            curr_node = BinarySearchTreeMap.Node(new_item)
            if val_to_insert is not None and curr_node.item.key > val_to_insert and connect_pos is None:
                connect_pos = prev_node
            curr_node.left = prev_node
            prev_node.parent = curr_node
            if start_pos == 0:
                if connect_pos is None:  # if connect position is None, then the connect position should be the root of the subtree
                    return curr_node, curr_node
                return connect_pos, curr_node
        prev_connect_pos, curr_root = restore_bst_helper(
            prefix_lst, start_pos - 1, curr_node.item.key)
        prev_connect_pos.right = curr_node
        # connect current subtree to the returned subtree
        curr_node.parent = prev_connect_pos
        if connect_pos is None:
            connect_pos = curr_node
        if val_to_insert is not None and val_to_insert > curr_root.item.key > connect_pos.item.key:
            # process the edge case in which current subtree should connect to the root
            return curr_root, curr_root
        return connect_pos, curr_root
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.root = restore_bst_helper(prefix_lst, len(prefix_lst) - 1, None)[1]
    bst.size = len(prefix_lst)
    return bst
