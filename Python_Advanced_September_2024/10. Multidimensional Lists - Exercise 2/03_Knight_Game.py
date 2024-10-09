rows = int(input())
matrix = [[x for x in list(input())] for _ in range(rows)]


def is_in_matrix(i, j):
    return 0 <= i < rows and 0 <= j < rows


def print_matrix(m):
    for r in m:
        print(f"{''.join([x for x in r])}")


directions = ((-1, -2),
              (-2, -1),
              (-2, 1),
              (-1, 2),
              (1, 2),
              (2, 1),
              (2, -1),
              (1, -2))
knights = []
removed = 0


for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == "K":
            knights.append([i, j])

while True:
    max_attacks = 0
    max_knight = []
    for knight in knights:
        attacks = 0
        for move in directions:
            next_row = knight[0] + move[0]
            next_col = knight[1] + move[1]
            if is_in_matrix(next_row, next_col):
                if matrix[next_row][next_col] == "K":
                    attacks += 1
        if attacks > max_attacks:
            max_attacks = attacks
            max_knight = knight
    if max_attacks > 0:
        matrix[max_knight[0]][max_knight[1]] = "0"
        knights.remove(max_knight)
        removed += 1
    else:
        break

print(removed)
