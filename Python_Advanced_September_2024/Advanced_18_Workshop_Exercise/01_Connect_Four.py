class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(ma):
    for el in ma:
        print(f"| {' | '.join([str(x) for x in el])} |")
    print("--^-" * 7 + "-")


def is_winner(ma, r, c, player_n, slots=4):
    if any([
        is_horizontal_win(ma, r, c, player_n, slots),
        is_vertical_win(ma, r, c, player_n, slots),
        is_right_diagonal_win(ma, r, c, player_n, slots),
        is_left_diagonal_win(ma, r, c, player_n, slots)
    ]):
        return True
    return False


def validate_column_choice(col_num, size):
    if not (0 <= col_num < size):
        raise InvalidColumnError()


def place_player_choice(ma, col_index, player_n):
    for row_index in range(len(ma) - 1, -1, -1):
        current_el = ma[row_index][col_index]
        if current_el == 0:
            ma[row_index][col_index] = player_n
            return row_index, col_index
    raise FullColumnError()


def is_vertical_win(ma, r, c, player_n, slots):
    return all([is_player_number(ma, r + idx, c, player_n) for idx in range(slots)])


def is_horizontal_win(ma, r, c, player_n, slots):
    right = []
    left = []
    for idx in range(slots):
        if is_player_number(ma, r, c + idx, player_n):
            right.append(True)
        else:
            break
    for idx in range(slots):
        if is_player_number(ma, r, c - idx, player_n):
            left.append(True)
        else:
            break
    return len(left + right) > slots


def is_right_diagonal_win(ma, r, c, player_n, slots):
    right_up = []
    left_down = []
    for idx in range(slots):
        if is_player_number(ma, r - idx, c + idx, player_n):
            right_up.append(True)
        else:
            break
    for idx in range(slots):
        if is_player_number(ma, r + idx, c - idx, player_n):
            left_down.append(True)
        else:
            break
    return len(left_down + right_up) > slots


def is_left_diagonal_win(ma, r, c, player_n, slots):
    left_up = []
    right_down = []
    for idx in range(slots):
        if is_player_number(ma, r - idx, c - idx, player_n):
            left_up.append(True)
        else:
            break
    for idx in range(slots):
        if is_player_number(ma, r + idx, c + idx, player_n):
            right_down.append(True)
        else:
            break
    return len(right_down + left_up) > slots


# def is_right_diagonal_win(ma, r, c, player_n, slots):
#     right_up = [is_player_number(ma, r - idx, c + idx, player_n) for idx in range(slots)].count(True)
#     left_down = [is_player_number(ma, r + idx, c - idx, player_n) for idx in range(slots)].count(True)
#     return (right_up + left_down) > slots
#
#
# def is_left_diagonal_win(ma, r, c, player_n, slots):
#     left_up = [is_player_number(ma, r - idx, c - idx, player_n) for idx in range(slots)].count(True)
#     right_down = [is_player_number(ma, r + idx, c + idx, player_n) for idx in range(slots)].count(True)
#     return (left_up + right_down) > slots


def is_player_number(ma, r, c, player_n):
    if c < 0 or r < 0:
        return False
    try:
        if ma[r][c] == player_n:
            return True
    except IndexError:
        return False
    return False


rows_count = 6
cols_count = 7

matrix = [[0 for col in range(cols_count)] for row in range(rows_count)]

print_matrix(matrix)

player_num = 1
counter = 0

while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        column_number = int(input(f"Player {player_num}, please choose a column [1-{cols_count}]: ")) - 1
        validate_column_choice(column_number, cols_count)
        row, col = place_player_choice(matrix, column_number, player_num)
        print_matrix(matrix)

        if is_winner(matrix, row, col, player_num):
            print(f"The winner is player {player_num}!")
            break
    except ValueError:
        print(f"Not a number! Please choose correct number from 1 to {cols_count}!")
        continue
    except InvalidColumnError:
        print(f"Please choose correct column number from 1 to {cols_count}!")
        continue
    except FullColumnError:
        print(f"Please choose an empty column number!")
        continue
    counter += 1
    if rows_count * cols_count == counter:
        print("The game is draw!")
        break
    player_num += 1
