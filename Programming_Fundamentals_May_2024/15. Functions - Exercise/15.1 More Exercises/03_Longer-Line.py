import math


def dist_to_center(x, y):
    return math.sqrt(x**2 + y**2)


def dist_between_points(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1-y2) ** 2)


def closer_to_center(x1, y1, x2, y2):
    if dist_to_center(x1, y1) <= dist_to_center(x2, y2):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


def further_to_center(x1, y1, x2, y2):
    if dist_to_center(x1, y1) > dist_to_center(x2, y2):
        return f"({math.floor(x1)}, {math.floor(y1)})"
    else:
        return f"({math.floor(x2)}, {math.floor(y2)})"


def longer_line(a, b):
    if dist_between_points(a[0], a[1], a[2], a[3]) >= dist_between_points(b[0], b[1], b[2], b[3]):
        return a
    else:
        return b


x11 = float(input())
y11 = float(input())
x12 = float(input())
y12 = float(input())
x21 = float(input())
y21 = float(input())
x22 = float(input())
y22 = float(input())

first = [x11, y11, x12, y12]
second = [x21, y21, x22, y22]
result = longer_line(first, second)

print(f"{closer_to_center(result[0], result[1], result[2], result[3])}", end="")
print(f"{further_to_center(result[0], result[1], result[2], result[3])}")

