import math

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_matrix = []
max_sum = - math.inf


def matrix_sum(m):
    mat_sum = 0
    for row in m:
        mat_sum += sum(row)
    return mat_sum


def print_matrix(m):
    for row in m:
        print(f"{' '.join([str(x) for x in row])}")


for i in range(0, rows - 2):
    for j in range(0, cols - 2):
        test_matrix = []
        for k in range(3):
            test_row = []
            for p in range(3):
                test_row.append(matrix[i + k][j + p])
            test_matrix.append(test_row)

        current_sum = matrix_sum(test_matrix)
        if max_sum < current_sum:
            max_sum = current_sum
            max_matrix = test_matrix

print(f"Sum = {max_sum}")
print_matrix(max_matrix)
