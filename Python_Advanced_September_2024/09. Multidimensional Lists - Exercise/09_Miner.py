from collections import deque
size = int(input())
commands = deque(input().split())
matrix = [[x for x in input().split()] for _ in range(size)]
coal = 0
ended = False

position = []
for i in range(size):
    for j in range(size):
        if matrix[i][j] == "s":
            position = [i, j]
        elif matrix[i][j] == "c":
            coal += 1

while commands:
    current = commands.popleft()
    if current == "up":
        if position[0] >= 1:
            position[0] -= 1
    elif current == "right":
        if position[1] < size - 1:
            position[1] += 1
    elif current == "down":
        if position[0] < size - 1:
            position[0] += 1
    elif current == "left":
        if position[1] >= 1:
            position[1] -= 1

    if matrix[position[0]][position[1]] == "e":
        print(f"Game over! ({position[0]}, {position[1]})")
        ended = True
        break
    elif matrix[position[0]][position[1]] == "c":
        matrix[position[0]][position[1]] = "*"
        coal -= 1

if not ended:
    if coal <= 0:
        print(f"You collected all coal! ({position[0]}, {position[1]})")
    else:
        print(f"{coal} pieces of coal left. ({position[0]}, {position[1]})")
