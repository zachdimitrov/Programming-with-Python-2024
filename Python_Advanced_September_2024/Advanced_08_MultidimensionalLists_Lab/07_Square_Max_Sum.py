rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
# print(matrix)
max_matrix = []
max_sum = 0


def matrix_sum(m):
    mat_sum = 0
    for row in m:
        mat_sum += sum(row)
    return mat_sum


def print_matrix(m):
    for row in m:
        print(f"{' '.join([str(x) for x in row])}")


for i in range(0, rows - 1):
    for j in range(0, cols - 1):
        test_matrix = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        current_sum = matrix_sum(test_matrix)
        if max_sum < current_sum:
            max_sum = current_sum
            max_matrix = test_matrix

print_matrix(max_matrix)
print(max_sum)
