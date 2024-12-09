rows, cols = [int(x) for x in input().split(", ")]
matrix = []
matrix_sum = 0

for i in range(rows):
    col = [int(x) for x in input().split(", ")]
    matrix.append(col)
    matrix_sum += sum(col)

print(matrix_sum)
print(matrix)
