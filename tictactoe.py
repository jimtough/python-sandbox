import random


def display_board(board):
    pass


def player_input():
    """
    Function that can take in a player input and assign their marker as 'X' or 'O'
    :return: "X" or "O"
    """
    pass


def place_marker(board, marker, position):
    """
    Function that takes in the board list object, a marker ('X' or 'O'),
    and a desired position (number 1-9) and assigns it to the board
    :param board: array
    :param marker: string
    :param position: int
    """
    pass


def win_check(board, mark):
    """
    Function that takes in a board and a mark (X or O) and then checks to see if that mark has won
    :param board: array
    :param mark: string
    :return: boolean
    """
    pass


def choose_first():
    """
    Function that uses the random module to randomly decide which player goes first.
    Return a string of which player went first.
    :return:
    """
    #You may want to lookup random.randint()
    pass


def space_check(board, position):
    """
    Function that returns a boolean indicating whether a space on the board is freely available.
    :param board: array
    :param position: int
    :return: boolean
    """
    pass


def full_board_check(board):
    """
    Function that checks if the board is full and returns a boolean value. True if full, False otherwise.
    :param board:
    :return:
    """
    pass


def player_choice(board):
    """
    Function that asks for a player's next position (as a number 1-9) and then uses the 'space_check()' function
    to check if it's a free position. If it is, then return the position for later use.
    :param board: array
    :return: boolean
    """
    pass


def replay():
    """
    Function that asks the player if they want to play again and returns a boolean True if they do want to play again.
    :return: boolean
    """
    pass


print('Welcome to Tic Tac Toe!')

# while True:
# Set the game up here
# pass

# while game_on:
# Player 1 Turn


# Player2's turn.

# pass

# if not replay():
# break

#test_board = ['#','X','O','X','O','X','O','X','O','X']
test_board = ['X','O','X','O','X','O','X','O','X']
display_board(test_board)
#player_input()
#place_marker(test_board,'$',8)
#display_board(test_board)
#win_check(test_board,'X')
