from ArrayStack import ArrayStack
import sys
sys.path.append(sys.path[0] + '/../DataStructure')


def stack_sum(s):
    if len(s) == 1:
        return s.top()
    for i in range(len(s)):
        val = s.pop()
        sum = stack_sum(s)
        sum += val
        s.push(val)
        return sum


def eval_prefix(exp_str):
    exp = exp_str.split()
    args_stack = ArrayStack()
    for i in range(len(exp)):
        token = exp.pop()
        if token in "+-*/":
            arg1 = args_stack.pop()
            arg2 = args_stack.pop()
            if arg2 == "0" and token == "/":
                raise ZeroDivisionError
            else:
                res = eval(str(arg1) + token + str(arg2))
            args_stack.push(int(res))
        else:
            args_stack.push(int(token))
    return args_stack.pop()


def is_balanced(input_str):
    char_stack = ArrayStack()
    for char in input_str:
        if char in "([{":
            char_stack.push(char)
        else:
            if len(char_stack) == 0:
                return False
            left_part = char_stack.pop()
            if not (left_part == "(" and char == ")" or left_part == "["
                    and char == "]" or left_part == "{" and char == "}"):
                return False
    if len(char_stack) != 0:
        return False
    return True


def is_balanced2(input_str):
    char_stack = ArrayStack()
    for char in input_str:
        if char == "(":
            char_stack.push(char)
        else:
            if len(char_stack) == 0:
                return False
            left_part = char_stack.pop()
            if left_part != "(":
                return False
    if len(char_stack) != 0:
        return False
    return True


def flatten_list(lst):
    helper_stack = ArrayStack()
    isFlattened = False
    while not isFlattened:
        isFlattened = True
        for i in range(len(lst)):
            helper_stack.push(lst.pop())
        for i in range(len(helper_stack)):
            val = helper_stack.pop()
            if isinstance(val, list):
                isFlattened = False
                for elem in val:
                    lst.append(elem)
            else:
                lst.append(val)


def stack_sort(s):
    helper_stack = ArrayStack()
    for i in range(len(s)):
        val = s.pop()
        count = 0
        while not helper_stack.is_empty() and val < helper_stack.top():
            s.push(helper_stack.pop())
            count += 1
        helper_stack.push(val)
        for i in range(count):
            helper_stack.push(s.pop())
    for i in range(len(helper_stack)):
        s.push(helper_stack.pop())
