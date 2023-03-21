import tic_tac_toe
import pytest

# Tests that a board is printed correctly
def test_print_board():
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    assert tic_tac_toe.print_board() == print(board[0] + " | " + board[1] + " | " + board[2])
    assert tic_tac_toe.print_board() == print(board[3] + " | " + board[4] + " | " + board[5])
    assert tic_tac_toe.print_board() == print(board[6] + " | " + board[7] + " | " + board[8])
    
    
# Tests that the player can input a valid position
#def test_player_input():


# Tests if current player has won horizontally    
#def test_check_horizontal():

    
# Tests if current player has won vertically
#def test_check_vertical():
