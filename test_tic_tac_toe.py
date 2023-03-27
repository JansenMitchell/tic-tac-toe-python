import tic_tac_toe
import pytest

def test_draw_board():
    board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    expected = ('-' * 13 + '| X | O | X |' + '-' * 13 + '| O | X | O |' + '-' * 13 + '| X | O | X |' + '-' * 13)
