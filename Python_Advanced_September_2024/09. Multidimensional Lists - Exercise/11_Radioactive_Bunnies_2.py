rows, cols = [int(x) for x in input().split()]
liar = [[x for x in list(input())] for _ in range(rows)]

commands = list(input())

directions = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


def is_in_matrix(i, j):
    return 0 <= i < rows and 0 <= j < cols


def print_matrix(m):
    for r in m:
        print(f"{''.join([x for x in r])}")


position = []
bunnies = []
dead = False
won = False

for i in range(rows):
    for j in range(cols):
        if liar[i][j] == "P":
            position = [i, j]
        elif liar[i][j] == "B":
            bunnies.append([i, j])

for command in commands:
    if dead or won:
        break
    x = position[0] + directions[command][0]
    y = position[1] + directions[command][1]
    liar[position[0]][position[1]] = "."
    if is_in_matrix(x, y):
        if liar[x][y] == ".":
            liar[x][y] = "P"
            position = [x, y]
        else:
            position = [x, y]
            dead = True
    else:
        won = True

    new_bunnies = []
    for bunny in bunnies:
        for val in directions.values():
            x = bunny[0] + val[0]
            y = bunny[1] + val[1]
            if is_in_matrix(x, y):
                liar[x][y] = "B"
                new_bunnies.append([x, y])
                if x == position[0] and y == position[1]:
                    dead = True
    bunnies.extend(new_bunnies)

print_matrix(liar)
if dead:
    print(f"dead: {position[0]} {position[1]}")
else:
    print(f"won: {position[0]} {position[1]}")
