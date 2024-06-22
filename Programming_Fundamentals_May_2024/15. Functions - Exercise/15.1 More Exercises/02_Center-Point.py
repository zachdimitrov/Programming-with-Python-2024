import math


def dist_to_center(x, y):
    return math.sqrt(x**2 + y**2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if dist_to_center(x1, y1) <= dist_to_center(x2, y2):
    print(f"({math. floor(x1)}, {math. floor(y1)})")
else:
    print(f"({math. floor(x2)}, {math. floor(y2)})")
