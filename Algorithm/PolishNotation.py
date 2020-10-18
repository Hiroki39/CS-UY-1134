import sys
sys.path.append(sys.path[0] + "/../DataStructure")
from ArrayStack import ArrayStack


def eval_postfix_exp(exp_str):
    exp = exp_str.split()
    args_stack = ArrayStack()
    for token in exp:
        if token in "+-*/":
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if arg2 == "0" and token == "/":
                raise ZeroDivisionError
            else:
                res = eval(arg1 + token + arg2)
            args_stack.push(res)
        else:
            args_stack.push(token)
    return int(args_stack.pop())
