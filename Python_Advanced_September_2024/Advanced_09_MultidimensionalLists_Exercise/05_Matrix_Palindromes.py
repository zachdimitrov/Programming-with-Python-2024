rows, cols = [int(x) for x in input().split()]

start = ord("a")
matrix = []


def print_matrix(m):
    for r in m:
        print(f"{' '.join([str(x) for x in r])}")


for i in range(rows):
    row = []
    word = ""
    for j in range(cols):
        word = f"{chr(start + i)}{chr(start + i + j)}{chr(start + i)}"
        row.append(word)
    matrix.append(row)

print_matrix(matrix)