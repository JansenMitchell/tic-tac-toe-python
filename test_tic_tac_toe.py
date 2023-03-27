import tic_tac_toe
import pytest

def test_draw_board():
    board = [' '] * 10
    board[1] = 'X'
    board[2] = 'O'
    board[3] = 'X'
    board[4] = 'O'
    board[5] = 'X'
    board[6] = 'O'
    board[7] = 'X'
    board[8] = 'O'
    board[9] = 'X'
    tic_tac_toe.draw_board(board)
    assert board[1] == 'X'
    assert board[2] == 'O'
    assert board[3] == 'X'
    assert board[4] == 'O'
    assert board[5] == 'X'
    assert board[6] == 'O'
    assert board[7] == 'X'
    assert board[8] == 'O'
    assert board[9] == 'X'
    
def test_is_space_free():
    board = [' '] * 10
    board[1] = 'X'
    board[2] = 'O'
    board[3] = 'X'
    board[4] = 'O'
    board[5] = 'X'
    board[6] = 'O'
    board[7] = 'X'
    board[8] = 'O'
    board[9] = 'X'
    assert tic_tac_toe.is_space_free(board, 1) == False
    assert tic_tac_toe.is_space_free(board, 2) == False
    assert tic_tac_toe.is_space_free(board, 3) == False
    assert tic_tac_toe.is_space_free(board, 4) == False
    assert tic_tac_toe.is_space_free(board, 5) == False
    assert tic_tac_toe.is_space_free(board, 6) == False
    assert tic_tac_toe.is_space_free(board, 7) == False
    assert tic_tac_toe.is_space_free(board, 8) == False
    assert tic_tac_toe.is_space_free(board, 9) == False