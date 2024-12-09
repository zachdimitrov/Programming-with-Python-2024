# Full name of task: 10. *Radioactive Mutant Vampire Bunnies
from collections import deque

rows, cols = [int(x) for x in input().split()]
liar = [[x for x in list(input())] for _ in range(rows)]
commands = deque(list(input()))
buns = set()
escaped = False


def print_matrix(m):
    for r in m:
        print(f"{''.join([x for x in r])}")


position = []
for i in range(rows):
    for j in range(cols):
        if liar[i][j] == "P":
            position = [i, j]
            liar[position[0]][position[1]] = "."
        elif liar[i][j] == "B":
            buns.add((i, j))

while commands:
    new_buns = set()
    for bun in buns:
        if bun[0] > 0:
            liar[bun[0] - 1][bun[1]] = "B"
            new_buns.add((bun[0] - 1, bun[1]))
        if bun[0] < rows - 1:
            liar[bun[0] + 1][bun[1]] = "B"
            new_buns.add((bun[0] + 1, bun[1]))
        if bun[1] > 0:
            liar[bun[0]][bun[1] - 1] = "B"
            new_buns.add((bun[0], bun[1] - 1))
        if bun[1] < cols - 1:
            liar[bun[0]][bun[1] + 1] = "B"
            new_buns.add((bun[0], bun[1] + 1))

    current = commands.popleft()
    if current == "U":
        if position[0] > 0:
            position[0] -= 1
        else:
            escaped = True
    elif current == "R":
        if position[1] < cols - 1:
            position[1] += 1
        else:
            escaped = True
    elif current == "D":
        if position[0] < rows - 1:
            position[0] += 1
        else:
            escaped = True
    elif current == "L":
        if position[1] > 0:
            position[1] -= 1
        else:
            escaped = True

    if liar[position[0]][position[1]] == "B":
        print_matrix(liar)
        print(f"dead: {position[0]} {position[1]}")
        break
    if escaped:
        print_matrix(liar)
        print(f"won: {position[0]} {position[1]}")
        break
    buns = buns.union(new_buns)
