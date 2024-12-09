n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]


def is_in_matrix(i, j):
    return 0 <= i < n and 0 <= j < n


def print_matrix(m):
    for r in m:
        print(f"{' '.join([x for x in r])}")


alice = []
tea = 0
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
for i in range(n):
    for j in range(n):
        if matrix[i][j] == "A":
            alice = [i, j]

matrix[alice[0]][alice[1]] = "*"
while True:
    direction = directions[input()]
    x = alice[0] + direction[0]
    y = alice[1] + direction[1]
    if is_in_matrix(x, y):
        if matrix[x][y] != "R":
            if matrix[x][y].isnumeric():
                tea += int(matrix[x][y])
            alice = [x, y]
            matrix[x][y] = "*"
        else:
            matrix[x][y] = "*"
            break
    else:
        break
    if tea >= 10:
        break
if tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
print_matrix(matrix)
