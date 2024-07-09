def find_position(maze):
    position = []
    for row in range(len(maze)):
        for elm in maze[row]:
            if elm == "k":
                position.append(row)
                position.append(maze[row].index("k"))
    return position


def next_free_position(maze):
    free_spots = []
    for row in range(len(maze)):
        for el in range(len(maze[row])):
            if maze[row][el] == ' ':
                free_spots.append([row, el])
    return free_spots


def get_path(position, next_free, maze):
    moves = 0
    found = False
    checked = []

    while len(next_free) > 0:
        x1, x2 = next_free.pop(0)

        if position[0] == x1 and position[1] - x2 == 1: #ako mojem se mestim nalqvo
            found = True
        if position[0] == x1 and x2 - position[1] == 1: #dqsno
            found = True
        if position[0] - x1 == 1 and position[1] == x2: #gore
            found = True
        if x1 - position[0] == 1 and position[1] == x2: #dolu
            found = True

        if found:
            moves += 1
            if checked.count(position) < 3:
                next_free.append(position)
                checked.append(position)
            position = [x1, x2]
            found = False
        else:
            if checked.count([x1, x2]) < 3:
                next_free.append([x1, x2])
                checked.append([x1, x2])

        if position[0] == 0 or position[0] == len(maze) - 1 or position[1] == 0 or position[1] == len(maze[0]) - 1:
            return f'Kate got out in {moves + 1} moves'

    return "Kate cannot get out"


rows = int(input())
maze = []
for j in range(rows):
    maze_rows = [*input()]
    maze.append(maze_rows)

initial_position = find_position(maze)
next_free = next_free_position(maze)
move = get_path(initial_position, next_free, maze)

print(move)

"""
3
###
#k#
###

4
# #
#k#
# #
# #

4
####
# k#
## #
## #

8
#######
## k###
## ##
## ## #
#  ## #
# ### #
#     #
#######
"""