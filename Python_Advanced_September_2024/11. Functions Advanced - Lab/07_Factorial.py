def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


print(fact(5))
print(fact(10))
print(fact(21))