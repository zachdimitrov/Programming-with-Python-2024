rows, cols = [int(x) for x in input().split(", ")]
matrix = [[c for c in input()] for _ in range(rows)]
seconds = 16
on_bomb = False


def print_matrix(m):
    for r in m:
        print(f"{''.join([str(x) for x in r])}")


def find_player(m, r, c, symbol):
    p = []
    for a in range(r):
        for b in range(c):
            if m[a][b] == symbol:
                p = [a, b]
    return p


def move_player(p, r, c, d):
    if 0 <= (p[0] + d[0]) < r and 0 <= (p[1] + d[1]) < c:
        return [p[0] + d[0], p[1] + d[1]]
    else:
        return p


directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
counter_terrorist = find_player(matrix, rows, cols, "C")
new_position = counter_terrorist
command = input()

while True:
    if command in directions:
        new_position = move_player(counter_terrorist, rows, cols, directions[command])
        seconds -= 1
        if matrix[new_position[0]][new_position[1]] == "B":
            counter_terrorist = new_position
            on_bomb = True
        else:
            on_bomb = False
        if matrix[new_position[0]][new_position[1]] == "T":
            matrix[new_position[0]][new_position[1]] = "*"
            print("Terrorists win!")
            print_matrix(matrix)
            break
        if matrix[new_position[0]][new_position[1]] == "*":
            counter_terrorist = new_position
    if command == "defuse":
        if on_bomb:
            if seconds >= 4:
                seconds -= 4
                matrix[new_position[0]][new_position[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {seconds} second/s remaining.")
                print_matrix(matrix)
            else:
                matrix[new_position[0]][new_position[1]] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {4 - seconds} second/s.")
                print_matrix(matrix)
            break
        else:
            seconds -= 2
    if seconds <= 0:
        print("Terrorists win!")
        print("Bomb was not defused successfully!")
        print(f"Time needed: 0 second/s.")
        print_matrix(matrix)
        break
    command = input()
