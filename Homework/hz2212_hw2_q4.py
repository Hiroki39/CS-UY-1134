def e_approx(n):
    e = 1
    addend = 1
    for i in range(1, n + 1):
        addend = addend / i
        e = e + addend
    return e
