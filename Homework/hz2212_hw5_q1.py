import sys
sys.path.append(sys.path[0] + '/../DataStructure')
import copy
from ArrayStack import ArrayStack


input_str = input("-->")
on_start = True
while input_str != "done()":
    is_assign_exp = False
    input_lst = input_str.split()
    args_stack = ArrayStack()
    for token in input_lst:
        if token in "+-*/":
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if arg2 == "0" and token == "/":
                raise ZeroDivisionError
            result = eval(arg1 + token + arg2)
            args_stack.push(str(result))
        elif token == "=":
            var_name = args_stack.pop()
            is_assign_exp = True
        else:
            args_stack.push(token)
    submit = eval(args_stack.pop())  # Convert string to int or float
    if is_assign_exp:
        if on_start:  # get a dict whose keys are program variables
            program_var = copy.copy(locals())
            on_start = False
        if var_name in program_var or var_name == "program_var":
            print("please try another variable name")  # prevent overriding
        else:
            locals()[var_name] = submit  # set variables from user input
            print(var_name)
    else:
        print(submit)
    input_str = input("-->")
