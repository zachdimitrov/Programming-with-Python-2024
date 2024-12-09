matrix = [[x for x in input().split()] for _ in range(5)]


def is_in_matrix(i, j):
    return 0 <= i < 5 and 0 <= j < 5


def print_matrix(m):
    for r in m:
        print(f"{' '.join([x for x in r])}")


shooter = []
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
n = int(input())
targets_shot = []
targets = 0

for i in range(5):
    for j in range(5):
        if matrix[i][j] == "A":
            shooter = [i, j]
        elif matrix[i][j] == "x":
            targets += 1

for _ in range(n):
    commands = input().split()
    command = commands[0]
    if command == "move":
        direction = commands[1]
        steps = int(commands[2])
        x, y = directions[direction]
        new_x = shooter[0] + x * steps
        new_y = shooter[1] + y * steps
        if is_in_matrix(new_x, new_y) and matrix[new_x][new_y] == ".":
            matrix[new_x][new_y] = "A"
            matrix[shooter[0]][shooter[1]] = "."
            shooter = [new_x, new_y]
    elif command == "shoot":
        direction = commands[1]
        x, y = directions[direction]
        row = shooter[0] + x
        col = shooter[1] + y
        while is_in_matrix(row, col):
            if matrix[row][col] == "x":
                targets_shot.append([row, col])
                matrix[row][col] = "."
                break
            row += x
            col += y
        if len(targets_shot) >= targets:
            print(f"Training completed! All {targets} targets hit.")
            break

#print_matrix(matrix)
if len(targets_shot) < targets:
    print(f"Training not completed! {targets - len(targets_shot)} targets left.")
for t in targets_shot:
    print(t)
