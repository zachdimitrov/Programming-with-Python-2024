n = int(input())
matrix = []
hero_position = ()
health = 100
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row_index in range(n):
    row_data = list(input())
    if "P" in row_data:
        col_index = row_data.index("P")
        hero_position = (row_index, col_index)
    matrix.append(row_data)

while True:
    direction = input()
    next_row = hero_position[0] + directions[direction][0]
    if next_row < 0 or next_row > n - 1:
        continue

    next_col = hero_position[1] + directions[direction][1]
    if next_col < 0 or next_col > n - 1:
        continue

    if matrix[next_row][next_col] == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            matrix[next_row][next_col] = "P"
            matrix[hero_position[0]][hero_position[1]] = "-"
            hero_position = (next_row, next_col)
            break
    elif matrix[next_row][next_col] == "H":
        health += 15
        if health > 100:
            health = 100
    elif matrix[next_row][next_col] == "X":
        print("Player escaped the maze. Danger passed!")
        matrix[next_row][next_col] = "P"
        matrix[hero_position[0]][hero_position[1]] = "-"
        hero_position = (next_row, next_col)
        break
    matrix[next_row][next_col] = "P"
    matrix[hero_position[0]][hero_position[1]] = "-"
    hero_position = (next_row, next_col)

print(f"Player's health: {health} units")
for row in matrix:
    print(*row, sep="")

