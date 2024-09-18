rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for i in range(cols):
    col_sum = 0
    for row in matrix:
        col_sum += row[i]
    print(col_sum)
