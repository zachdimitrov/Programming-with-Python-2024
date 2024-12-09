rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


def print_matrix(m):
    for r in m:
        print(f"{' '.join([str(x) for x in r])}")


line = input()
while line != "END":
    command = line.split()
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if 0 <= row < rows and 0 <= col < rows:
        if command[0] == "Add":
            matrix[row][col] += value
        elif command[0] == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    line = input()
print_matrix(matrix)