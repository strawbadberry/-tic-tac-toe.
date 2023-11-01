# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None.""" 

    winner = None

    # Check rows, columns, and diagonals
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] or
            board[0][i] == board[1][i] == board[2][i]):
            winner = board[i][0]

    


def other_player(player):
    """Given the character for a player, returns the other player."""
    if player == "X":
     return "0"
    elif player == "0":
     return "X"