def is_safe(board, row, col, visited):
    largest_row = len(board)
    largest_col = len(board[0])
    if 0 <= row < largest_row and \
        0 <= col < largest_col and \
            board[row][col] == "." and not visited[row][col]:
        return True
    else:
        return False


def dfs(maze, row, col, visited, count):
    row_neighbors = [0, 0, 1, -1]
    col_neighbors = [1, -1, 0, 0]
    visited[row][col] = True

    for k in range(4):
        if is_safe(maze, row + row_neighbors[k], col + col_neighbors[k], visited):
            count[0] += 1
            dfs(maze, row + row_neighbors[k], col + col_neighbors[k], visited, count)


def find_longest_path(maze):
    ROW = len(maze)
    COL = len(maze[0])
    final = -1

    visited = [[0] * COL for i in range(ROW)]
    for i in range(ROW):
        for j in range(COL):
            if maze[i][j] == "." and not visited[i][j]:
                count = [1]
                dfs(maze, i, j, visited, count)
                final = max(final, count[0])
    return final


n_rows = int(input())
board = []
for j in range(n_rows):
    board.append(input().split(" "))

result = find_longest_path(board)
print(result)
