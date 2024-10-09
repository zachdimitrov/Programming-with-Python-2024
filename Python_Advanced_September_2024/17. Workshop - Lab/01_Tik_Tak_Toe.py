from math import ceil


class InvalidNumberError(Exception):
    pass


class InvalidValueNumberError(Exception):
    pass


class UnavailablePositionError(Exception):
    pass


current_player = None


def define_signs(name):
    while True:
        sign = input(f"{name} would you like to play with X or O?: ")
        if sign in "xOxo":
            break
    other_player_sign = "O" if sign in "Xx" else "X"
    return sign, other_player_sign


def setup_players():
    player_one_name = input("Player one name: ")
    player_two_name = input("Player two name: ")
    player_one_sign, player_two_sign = define_signs(player_one_name)
    player_one = (player_one_name, player_one_sign)
    player_two = (player_two_name, player_two_sign)
    return player_one, player_two


def check_position_availability(position: int, board: list[list[str]]) -> tuple[int, int]:
    selected_row_index = ceil(position / 3) - 1
    selected_col_index = position % 3 - 1
    if board[selected_row_index][selected_col_index] != " ":
        print("Please enter a number for available position!")
        raise UnavailablePositionError
    return selected_row_index, selected_col_index


def check_position_validity(position: str) -> int:
    try:
        position = int(position)
    except ValueError:
        print("Please enter a valid number")
        raise InvalidNumberError
    if position < 1 or position > 9:
        print("Please enter a valid number between [1-9]!")
        raise InvalidValueNumberError

    return position


def print_board(board):
    for row in board:
        print(f"| {' | '.join([str(x) for x in row])} |")


player_one, player_two = setup_players()
num_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_board(num_board)

board = [[" ", " ", " "] for _ in range(3)]
print(f"{player_one[0]} starts first!")
turns = 1
while True:
    current_player = player_one if turns % 2 != 0 else player_two
    position = input(f"{current_player[0]} choose a free position [1-9]: ")

    try:
        position = check_position_validity(position)
        row_index, col_index = check_position_availability(position, board)
    except (InvalidValueNumberError, InvalidNumberError, UnavailablePositionError):
        print("Position should be [1-9]!")
        continue
    except UnavailablePositionError:
        print("You must select an empty position!")
    else:
        board[row_index][col_index] = current_player[1]
        print_board(board)
        turns += 1
        if turns >= 6:
            first_row = all([el == current_player[1] for el in board[0]])
            second_row = all([el == current_player[1] for el in board[1]])
            third_row = all([el == current_player[1] for el in board[2]])
            first_col = all([x == current_player[1] for x in [board[0][0], board[1][0], board[2][0]]])
            second_col = all([x == current_player[1] for x in [board[0][1], board[1][1], board[2][1]]])
            third_col = all([x == current_player[1] for x in [board[0][2], board[1][2], board[2][2]]])
            first_diag = all([x == current_player[1] for x in [board[0][0], board[1][1], board[2][2]]])
            second_diag = all([x == current_player[1] for x in [board[0][2], board[1][1], board[2][0]]])
            if any([first_row, second_row, third_row, first_col, second_col, third_col, first_diag, second_diag]):
                print(f"{current_player[0]} won!")
                break
        if turns == 9:
            print("DRAW! No one wins")
            break

#print(f"{current_player[0]} won!")
