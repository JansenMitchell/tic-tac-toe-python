import tic_tac_toe
import pytest

# Test board exists.
def test_board_init():
    board = tic_tac_toe.Board()
    assert board
    
# Test board is empty.
def test_board_is_empty():
    board = tic_tac_toe.Board()
    assert board.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Test board is full.
def test_board_is_full():
    board = tic_tac_toe.Board()
    board.board = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]
    assert board.is_full()

# Test board resets.
def test_board_reset():
    board = tic_tac_toe.Board()
    board.board = [["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]]
    board.reset()
    assert board.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Test board is printed as a 3x3 grid.

# Test board receives player 1 input.

# Test board receives player 2 input.

# Test player 1 exists.

# Test player 2 exists.

# Test game exists.

# Test horizontal win.

# Test vertical win.

# Test diagonal win.

# Test game is a draw.

# Test game is running.

# Test game is over.

# Test is player 1 is X.

# Test is player 2 is O.

# Test player 1 is human player.

# Test player 2 is ai player.

# Test player 1 has made a move.

# Test player 2 has made a move.

# Test player 2 makes optimal move (minimax).