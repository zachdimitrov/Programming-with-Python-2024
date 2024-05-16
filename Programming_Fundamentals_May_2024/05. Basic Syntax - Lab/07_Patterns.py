stars = int(input())
to_print = '*'
for i in range(0, stars):
    print(to_print)
    to_print += '*'
to_print = to_print[:-1]
for j in range(stars - 1, 0, -1):
    to_print = to_print[:-1]
    print(to_print)
