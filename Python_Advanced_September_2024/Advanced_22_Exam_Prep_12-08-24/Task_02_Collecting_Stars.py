def print_matrix(m):
    for r in m:
        print(f"{' '.join([str(x) for x in r])}")


def find_player(m, size, symbol):
    p = []
    for a in range(size):
        for b in range(size):
            if m[a][b] == symbol:
                p = [a, b]
    return p


def move_player(p, size, d):
    if 0 <= (p[0] + d[0]) < size and 0 <= (p[1] + d[1]) < size:
        return [p[0] + d[0], p[1] + d[1]]
    else:
        return [0, 0]


n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
player = find_player(matrix, n, "P")
stars = 2

while True:
    command = input()
    new_position = move_player(player, n, directions[command])
    element = matrix[new_position[0]][new_position[1]]
    if element == "*":
        stars += 1
        matrix[player[0]][player[1]] = "."
        player = new_position
        matrix[player[0]][player[1]] = "P"
    elif element == "#":
        stars -= 1
    elif element == ".":
        matrix[player[0]][player[1]] = "."
        player = new_position
        matrix[player[0]][player[1]] = "P"
    if stars <= 0:
        print(f"Game over! You are out of any stars.")
        print(f"Your final position is {player}")
        print_matrix(matrix)
        break
    if stars >= 10:
        print(f"You won! You have collected 10 stars.")
        print(f"Your final position is {player}")
        print_matrix(matrix)
        break
