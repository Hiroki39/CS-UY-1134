import sys
sys.path.append(sys.path[0] + '/../DataStructure')
from LinkedBinaryTree import LinkedBinaryTree


def create_expression_tree(prefix_exp_str):
    def create_expression_tree_helper(prefix_exp_lst, start_pos):
        token = prefix_exp_lst[start_pos]
        if token not in "+-*/":
            root = LinkedBinaryTree.Node(int(token))
            return (root, start_pos + 1)
        left_tup = create_expression_tree_helper(prefix_exp_lst, start_pos + 1)
        right_tup = create_expression_tree_helper(prefix_exp_lst, left_tup[1])
        root = LinkedBinaryTree.Node(token, left_tup[0], right_tup[0])
        return (root, right_tup[1])
    prefix_exp_lst = prefix_exp_str.split()
    return LinkedBinaryTree(create_expression_tree_helper(prefix_exp_lst, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    exp_tree = create_expression_tree(prefix_exp_str)
    postfix_exp_str = " ".join(str(node.data) for node in exp_tree.postorder())
    return postfix_exp_str
