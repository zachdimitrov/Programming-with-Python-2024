rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]


def print_matrix(m):
    for r in m:
        print(f"{' '.join([x for x in r])}")


def check_range(l):
    if l[0].isnumeric():
        a1 = int(l[0])
    else:
        return False
    if l[1].isnumeric():
        b1 = int(l[1])
    else:
        return False
    if l[2].isnumeric():
        a2 = int(l[2])
    else:
        return False
    if l[3].isnumeric():
        b2 = int(l[3])
    else:
        return False

    return 0 <= a1 < rows and 0 <= b1 < cols and 0 <= a2 < rows and 0 <= b2 < cols


command = input()
while command != "END":
    terms = command.split(" ", 1)
    if len(terms) > 1:
        coords = [x for x in terms[1].split()]
    else:
        print("Invalid input!")
        continue
    if terms[0] == "swap" and len(coords) == 4 and check_range(coords):
        x1, y1, x2, y2 = [int(x) for x in coords]
        k = matrix[x1][y1]
        matrix[x1][y1] = matrix[x2][y2]
        matrix[x2][y2] = k
        print_matrix(matrix)
    else:
        print("Invalid input!")
    command = input()
