n = int(input())
matrix = []
ship_position = ()
fuel = 100
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row_index in range(n):
    row_data = list(input().split())
    if "S" in row_data:
        col_index = row_data.index("S")
        ship_position = (row_index, col_index)
    matrix.append(row_data)

while True:
    direction = input()
    next_row = ship_position[0] + directions[direction][0]
    fuel -= 5
    if next_row < 0 or next_row > n - 1:
        print("Mission failed! The spaceship was lost in space.")
        break

    next_col = ship_position[1] + directions[direction][1]
    if next_col < 0 or next_col > n - 1:
        print("Mission failed! The spaceship was lost in space.")
        break

    if matrix[next_row][next_col] == "M":
        fuel -= 5
        matrix[next_row][next_col] = "S"
    elif matrix[next_row][next_col] == "R":
        fuel += 10
        if fuel > 100:
            fuel = 100
    elif matrix[next_row][next_col] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {fuel} resources left.")
        if matrix[ship_position[0]][ship_position[1]] != "R":
            matrix[ship_position[0]][ship_position[1]] = "."
        matrix[next_row][next_col] = "P"
        break
    elif matrix[next_row][next_col] == ".":
        matrix[next_row][next_col] = "S"

    if matrix[ship_position[0]][ship_position[1]] != "R":
        matrix[ship_position[0]][ship_position[1]] = "."
    ship_position = (next_row, next_col)

    if fuel < 5:
        print("Mission failed! The spaceship was stranded in space.")
        break

for row in matrix:
    print(*row, sep=" ")

