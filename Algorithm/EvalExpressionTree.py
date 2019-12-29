def eval_exp_tree(exp_tree):
    def eval_subtree(root):
        if root.left is None and root.right is None:
            return root.data
        left_arg = str(eval_subtree(root.left))
        right_arg = str(eval_subtree(root.right))
        if right_arg == "0" and root.data == "/":
            raise ZeroDivisionError
        return eval(left_arg + root.data + right_arg)
    return eval_subtree(exp_tree.root)
