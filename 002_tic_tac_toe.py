EMPTY = " "


def display_board(board):
    print('{}|{}|{}'.format(board[7], board[8], board[9]))
    print('{}|{}|{}'.format(board[4], board[5], board[6]))
    print('{}|{}|{}'.format(board[1], board[2], board[3]))


def player_input():
    """
    Function that can take in a player input and assign their marker as 'X' or 'O'
    :return: "X" or "O"
    """
    x_or_o = ''
    while x_or_o == '':
        s = input('Would you like to be X or O? ')
        if s.upper() == 'X':
            x_or_o = 'X'
        elif s.upper() == 'O':
            x_or_o = 'O'
        else:
            print("You may only choose X or O")
    return x_or_o


def place_marker(board, marker, position):
    """
    Function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board
    :param board: array
    :param marker: string
    :param position: int
    """
    board[position] = marker


def win_check(board, mark):
    """
    Function that takes in a board and a mark (X or O) and then checks to see if that mark has won
    :param board: array
    :param mark: string
    :return: boolean
    """

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the center
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal A
            (board[1] == mark and board[5] == mark and board[9] == mark) or  # diagonal B
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down left column
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down center column
            (board[9] == mark and board[6] == mark and board[3] == mark))  # down right column


# This is dumb. I'm skipping this feature. I know how to use a random number generator! Player 1 will always go first.
# def choose_first():
#     """
#     Function that uses the random module to randomly decide which player goes first.
#     Return a string of which player went first.
#     :return:
#     """
#     # You may want to lookup random.randint()
#     pass


def space_check(board, position):
    """
    Function that returns a boolean indicating whether a space on the board is freely available.
    :param board: array
    :param position: int
    :return: boolean
    """
    return board[position] == EMPTY


def full_board_check(board):
    """
    Function that checks if the board is full and returns a boolean value. True if full, False otherwise.
    :param board:
    :return:
    """
    if EMPTY in board[1:]:
        return False
    return True


def player_choice(board):
    """
    Function that asks for a player's next position (as a number 1-9) and then uses the 'space_check()' function
    to check if it's a free position. If it is, then return the position for later use.
    :param board: array
    :return: int
    """
    while True:
        s = input("Choose an empty board position (1-9 on numpad): ")
        if not s.isdigit():
            print('You must choose a position between 1 and 9 (inclusive).')
            continue
        pos = int(s)
        if 1 <= pos <= 9:
            if space_check(board, pos):
                return pos
            else:
                print('Position {} is already taken. You must choose again.'.format(pos))
                continue
        else:
            print('You must choose a position between 1 and 9 (inclusive).')


def replay():
    """
    Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
    :return: boolean
    """
    s = input('Would you like to play again? (y/N): ')
    return 'Y' == s.upper()


def do_player_turn(board, marker, player_number):
    """
    Do a player's turn, and return True if this player's turn wins the game, otherwise return False
    :param board: array
    :param marker: string
    :param player_number: int
    :return: True if this turn ends the game, otherwise False
    """
    display_board(game_board)
    print("Player {}'s turn".format(player_number))
    chosen_position = player_choice(board)
    place_marker(board, marker, chosen_position)
    if win_check(board, marker):
        display_board(game_board)
        print("Player {} WINS!".format(player_number))
        return True
    if full_board_check(game_board):
        display_board(game_board)
        print("Game ends in a DRAW. Nobody wins.")
        return True
    return False


# -------------------------------------------------------------------------------------------------
# THESE LINES ARE ONLY FOR TESTING METHODS ABOVE
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)
# player_input()
# place_marker(test_board, '$', 8)
# display_board(test_board)
# print(win_check(test_board, 'X'))
# print(full_board_check(test_board))
# -------------------------------------------------------------------------------------------------

print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    game_board = ['UNUSED!', EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
    print("Player 1 must choose a board marker")
    player_one_marker = player_input()
    player_two_marker = None
    if player_one_marker == 'X':
        player_two_marker = 'O'
    else:
        player_two_marker = 'X'
    print("Player 1 will play {} and Player 2 will play {}".format(player_one_marker, player_two_marker))

    while True:
        # Player 1 turn
        if do_player_turn(game_board, player_one_marker, 1):
            break
        # Player 2 turn
        if do_player_turn(game_board, player_two_marker, 2):
            break

    if not replay():
        break
