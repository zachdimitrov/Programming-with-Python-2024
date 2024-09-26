size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]
bombs = input().split()


def print_matrix(m):
    for r in m:
        print(f"{' '.join([str(x) for x in r])}")


for bomb in bombs:
    x, y = [int(x) for x in bomb.split(",")]
    if matrix[x][y] and matrix[x][y] > 0:
        value = matrix[x][y]
        matrix[x][y] = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + i < size and 0 <= y + j < size and matrix[x + i][y + j] > 0:
                    matrix[x + i][y + j] -= value
alive = 0
alive_sum = 0
for i in range(size):
    for j in range(size):
        value = matrix[i][j]
        if value > 0:
            alive += 1
            alive_sum += matrix[i][j]

print(f"Alive cells: {alive}")
print(f"Sum: {alive_sum}")
print_matrix(matrix)