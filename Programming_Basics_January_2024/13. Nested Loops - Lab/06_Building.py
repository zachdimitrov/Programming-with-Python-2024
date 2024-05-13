floors = int(input())
rooms = int(input())
to_print = ''

for room in range(0, rooms):
    to_print = to_print + f'L{floors}{room}'
    if room < rooms:
        to_print = to_print + ' '
print(to_print)
to_print = ''

for floor in range(floors - 1, 0, -1):
    for room in range(0, rooms):
        if floor % 2 == 0:
            to_print = to_print + f'O{floor}{room}'
            if room < rooms:
                to_print = to_print + ' '
        else:
            to_print = to_print + f'A{floor}{room}'
            if room < rooms:
                to_print = to_print + ' '
    print(to_print)
    to_print = ''

