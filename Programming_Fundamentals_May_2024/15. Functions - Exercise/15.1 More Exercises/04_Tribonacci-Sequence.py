n = int(input())


def tribonacci_complex(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    else:
        return tribonacci_complex(x - 1) + tribonacci_complex(x - 2) + tribonacci_complex(x - 3)


def tribonacci_simple(x):
    a = 1
    b = 1
    c = 2

    if x == 1:
        return a
    elif x == 2:
        return b
    elif x == 3:
        return c
    else:
        for i in range(3, x):
            d = a + b + c
            a = b
            b = c
            c = d
        return d


for i in range(1, n + 1):
    print(tribonacci_simple(i), end=" ")
