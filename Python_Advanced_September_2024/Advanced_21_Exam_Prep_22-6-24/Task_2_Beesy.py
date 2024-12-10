n = int(input())
matrix = [[x for x in input()] for _ in range(n)]


def print_matrix(m):
    for r in m:
        print(f"{''.join([str(x) for x in r])}")


bee = []
energy = 15
nectar = 0
nectar_needed = 30
restored = False
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "B":
            bee = [i, j]


def move_bee(b, row, col):
    new_row = b[0] + row
    if new_row >= n:
        new_row -= n
    elif new_row < 0:
        new_row += n

    new_col = b[1] + col
    if new_col >= n:
        new_col -= n
    elif new_col < 0:
        new_col += n
    return [new_row, new_col]


while True:
    command = input()
    energy -= 1
    if energy <= 0 and not restored:
        if nectar > nectar_needed:
            energy = energy + (nectar - nectar_needed)
            nectar = nectar_needed
            restored = True

    matrix[bee[0]][bee[1]] = "-"
    bee = move_bee(bee, *directions[command])
    symbol = matrix[bee[0]][bee[1]]
    matrix[bee[0]][bee[1]] = "B"

    if symbol.isnumeric():
        nectar += int(symbol)
    if symbol == "H":
        if nectar >= nectar_needed:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break
    if energy <= 0:
        print("This is the end! Beesy ran out of energy.")
        break

print_matrix(matrix)
