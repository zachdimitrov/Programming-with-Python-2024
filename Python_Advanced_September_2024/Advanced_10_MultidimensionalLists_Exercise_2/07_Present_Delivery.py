m = int(input())
n = int(input())
matrix = [[x for x in input().split()] for _ in range(n)]


def is_in_matrix(i, j):
    return 0 <= i < n and 0 <= j < n


def print_matrix(mt):
    for r in mt:
        print(f"{' '.join([x for x in r])}")


santa = []
nice_kids = 0
nice_kids_gifted = 0
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for i in range(n):
    for j in range(n):
        if matrix[i][j] == "S":
            santa = [i, j]
        elif matrix[i][j] == "V":
            nice_kids += 1

while True:
    if m == 0:
        break
    command = input()
    if command == "Christmas morning":
        break
    x, y = directions[command]
    next_x = santa[0] + x
    next_y = santa[1] + y
    if is_in_matrix(next_x, next_y):
        if matrix[next_x][next_y] == "V":
            m -= 1
            nice_kids_gifted += 1
        elif matrix[next_x][next_y] == "C":
            for dirn in directions.values():
                home_x = next_x + dirn[0]
                home_y = next_y + dirn[1]
                if is_in_matrix(home_x, home_y):
                    if matrix[home_x][home_y] in "VX" and m:
                        m -= 1
                        if matrix[home_x][home_y] == "V":
                            nice_kids_gifted += 1
                        matrix[home_x][home_y] = "-"
        matrix[santa[0]][santa[1]] = "-"
        matrix[next_x][next_y] = "S"
        santa = [next_x, next_y]

if m < 1 and nice_kids - nice_kids_gifted > 0:
    print("Santa ran out of presents!")
print_matrix(matrix)
if nice_kids_gifted >= nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - nice_kids_gifted} nice kid/s.")
