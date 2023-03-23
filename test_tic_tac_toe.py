import tic_tac_toe
import pytest

# a simple Tic Tac Toe program that satisfies the following requirements:
# It must have a UI so that I can play.  A console UI will do just fine.
# The program must play fair Tic Tac Toe against me
# The program must be unbeatable, and win every chance I give it

# Tests for the Board class.
def test_board_init():
    # Assigns a new board to the variable board.
    board = tic_tac_toe.Board()
    # Asserts that the board is a list of 9 zeros.
    assert board.board == [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Tests the display method.    
def test_board_display():
    board = tic_tac_toe.Board()
    assert board.display() == None
    
def test_board_update():
    board = tic_tac_toe.Board()
    # Calls the update method on the board object with the arguments 0 and 1.
    board.update(0, 1)
    assert board.board == [1, 0, 0, 0, 0, 0, 0, 0, 0]
    
def test_board_check_win():
    board = tic_tac_toe.Board()
    # Checks if the board has a winning row.
    board.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert board.check_win(1) == True
    # Checks if the board has a winning column.
    board.board = [1, 0, 0, 1, 0, 0, 1, 0, 0]
    assert board.check_win(1) == True
    # Checks if the board has a winning diagonal.
    board.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    assert board.check_win(1) == True
    # Checks if the board has no winning row, column, or diagonal.
    board.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert board.check_win(1) == False

def test_check_draw():
    board = tic_tac_toe.Board()
    # Checks if the board has an empty position.
    board.board = [1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert board.check_draw() == False
    # Checks if the board has no empty positions.
    board.board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert board.check_draw() == True
    
def test_check_game_over():
    board = tic_tac_toe.Board()
    # Checks if the board has a winning row.
    board.board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert board.check_game_over(1) == True
    # Checks if the board has a winning column.
    board.board = [1, 0, 0, 1, 0, 0, 1, 0, 0]
    assert board.check_game_over(1) == True
    # Checks if the board has a winning diagonal.
    board.board = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    assert board.check_game_over(1) == True
    # Checks if the board has no winning row, column, or diagonal.
    board.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert board.check_game_over(1) == False
    # Checks if the board has no empty positions.
    board.board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert board.check_game_over(1) == True
    
def test_reset():
    board = tic_tac_toe.Board()
    # Resets the board.
    board.board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    board.reset()
    assert board.board == [0, 0, 0, 0, 0, 0, 0, 0, 0]