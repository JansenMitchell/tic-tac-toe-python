import tic_tac_toe
import pytest

# a simple Tic Tac Toe program that satisfies the following requirements:
# It must have a UI so that I can play.  A console UI will do just fine.
# The program must play fair Tic Tac Toe against me
# The program must be unbeatable, and win every chance I give it

# Tests for the Board class.
# Test that the board is initialized correctly.
def test_board_init():
    board = tic_tac_toe.Board()
    assert board.board == [1, 2, 3, 4, 5, 6, 7, 8, 9]
   
# Test that the board can take in a move and mark it on the board.
def test_board_mark():
    board = tic_tac_toe.Board()
    board.mark(5, "X")
    assert board.board == [1, 2, 3, 4, "X", 6, 7, 8, 9]