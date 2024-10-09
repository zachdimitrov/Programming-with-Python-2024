rows = int(input())
matrix = [[x for x in input().split()] for _ in range(rows)]


def is_in_matrix(i, j):
    return 0 <= i < rows and 0 <= j < rows


bunny = []
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "B":
            bunny = [i, j]

max_eggs = 0
best_steps = []
best_direction = "up"

for key, val in directions.items():
    eggs = 0
    steps = []
    new_bunny = [bunny[0], bunny[1]]
    while True:
        new_bunny[0] += val[0]
        new_bunny[1] += val[1]
        if is_in_matrix(new_bunny[0], new_bunny[1]) and matrix[new_bunny[0]][new_bunny[1]] != "X":
            eggs += int(matrix[new_bunny[0]][new_bunny[1]])
            steps.append([new_bunny[0], new_bunny[1]])
        else:
            break
    if eggs >= max_eggs:
        max_eggs = eggs
        best_steps = steps
        best_direction = key

print(best_direction)
for st in best_steps:
    print(st)
print(max_eggs)
