n_rows = int(input())
arena = []
for n in range(n_rows):
    row = list(map(int, input().split()))
    arena.append(row)

squares_list = input().split()
squares_list = [list(map(int, sq.split("-"))) for sq in squares_list]

destroyed = 0

while True:
    if len(squares_list) == 0:
        print(destroyed)
        break
    row, col = squares_list.pop()
    if arena[row][col] > 0:
        arena[row][col] -= 1
        if arena[row][col] == 0:
            destroyed += 1

