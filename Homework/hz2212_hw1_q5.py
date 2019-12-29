def fibs(n):
    addend1 = 0
    addend2 = 1
    for i in range(n):
        sum = addend1 + addend2
        addend1 = addend2
        yield addend2
        addend2 = sum
