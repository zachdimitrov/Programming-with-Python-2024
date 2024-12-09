from collections import deque
cols, rows = [int(x) for x in input().split()]
snake = deque(input())
matrix = []


def print_matrix(m):
    for r in m:
        print(f"{''.join([x for x in r])}")


for i in range(0, cols):
    col = []
    for j in range(rows):
        symbol = snake.popleft()
        col.append(symbol)
        snake.append(symbol)

    if i % 2 != 0:
        col.reverse()
    matrix.append(col)

print_matrix(matrix)