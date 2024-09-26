rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

square_count = 0

for i in range(0, rows - 1):
    for j in range(0, cols - 1):
        symbol = matrix[i][j]
        if matrix[i][j] == symbol and \
            matrix[i][j + 1] == symbol and \
            matrix[i + 1][j] == symbol and \
            matrix[i + 1][j + 1] == symbol:
            square_count += 1

print(square_count)
