import numpy as np

"""
Minimal tic-tac-toe engine optimized for fast self-play training.

Board is a tuple of 9 ints: 0=empty, 1=X, -1=O.
Tuple representation allows direct use as dictionary key (for Q-table).
"""

# All winning lines: indices of three-in-a-row
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6),              # diagonals
)

EMPTY_BOARD = (0, 0, 0, 0, 0, 0, 0, 0, 0)

SYMBOLS = {0: ".", 1: "X", -1: "O"}


def print_board(board):
    """Print the board in a 3x3 grid."""
    for row in range(3):
        print(" ".join(SYMBOLS[board[row * 3 + col]] for col in range(3)))
    print()

def encode_board(board, player):
    """Encode the board in a player-relative format."""
    board = np.array(board)
    return np.concatenate([board == player, board == -player]).astype(np.float32)


def print_game(history, winner):
    """Print a full game replay from history."""
    for i, (board, player, action) in enumerate(history):
        print(f"Move {i + 1}: {SYMBOLS[player]} at position {action}")
        print_board(make_move(board, action, player))
    result = {1: "X wins", -1: "O wins", 0: "Draw"}
    print(result[winner])


def legal_moves(board):
    """Return list of indices where the board is empty."""
    return [i for i, v in enumerate(board) if v == 0]


def check_winner(board):
    """Return 1 if X wins, -1 if O wins, 0 if no winner yet."""
    for a, b, c in WIN_LINES:
        s = board[a] + board[b] + board[c]
        if s == 3:
            return 1
        if s == -3:
            return -1
    return 0


def is_draw(board):
    """Return True if the board is full with no winner."""
    return 0 not in board and check_winner(board) == 0


def make_move(board, action, player):
    """Return a new board with player's mark at action. No validation."""
    lst = list(board)
    lst[action] = player
    return tuple(lst)


def play_game(player_x_fn, player_o_fn):
    """
    Play a full game. player_x_fn and player_o_fn are callables:
        fn(board, player) -> action (int 0-8)

    Returns:
        winner: 1 (X wins), -1 (O wins), or 0 (draw)
        history: list of (board, player, action) for each move made
    """
    board = EMPTY_BOARD
    player = 1  # X goes first
    history = []

    while True:
        if player == 1:
            action = player_x_fn(board, player)
        else:
            action = player_o_fn(board, player)

        history.append((board, player, action))
        board = make_move(board, action, player)

        winner = check_winner(board)
        if winner != 0:
            return winner, history

        if is_draw(board):
            return 0, history

        player = -player
