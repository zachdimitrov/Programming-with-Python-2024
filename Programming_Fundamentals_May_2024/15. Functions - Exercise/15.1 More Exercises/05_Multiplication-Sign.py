def is_positive(a, b, c):
    positive = True

    for elem in [a, b, c]:
        if elem == 0:
            return "zero"
        elif elem < 0:
            if positive:
                positive = False
            else:
                positive = True

    if positive:
        return "positive"
    else:
        return "negative"


a1 = int(input())
b1 = int(input())
c1 = int(input())

print(is_positive(a1, b1, c1))
