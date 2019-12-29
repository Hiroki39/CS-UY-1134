def remove_all(lst, value):
    forward_step = 0
    for i in range(len(lst)):
        if lst[i] == value:
            forward_step += 1
        else:
            lst[i - forward_step] = lst[i]
    for i in range(forward_step):
        lst.pop()
