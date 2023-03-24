import tic_tac_toe
import pytest

# Test for Board class
def test_board_init():
    board = tic_tac_toe.Board()
    assert board.board == [' ' for _ in range(9)]

def test_board_draw():
    board = tic_tac_toe.Board()
    # Assert rows are printed correctly.
    assert board.draw() == print('   |   |   \n-----------\n   |   |   \n-----------\n   |   |   ')

def test_board_update():
    board = tic_tac_toe.Board()
    board.update(0, 'X')
    assert board.board[0] == 'X'
    
def test_board_is_empty():
    board = tic_tac_toe.Board()
    assert board.is_empty(0) == True
    
def test_board_is_full():
    board = tic_tac_toe.Board()
    board.board = ['X' for _ in range(9)]
    assert board.is_full() == True
    
def test_board_reset():
    board = tic_tac_toe.Board()
    board.board = ['X' for _ in range(9)]
    board.reset()
    assert board.board == [' ' for _ in range(9)]
    
# Test for Player class
def test_player_init():
    player = tic_tac_toe.Player('Player 1', 'X')
    assert player.name == 'Player 1'
    assert player.marker == 'X'