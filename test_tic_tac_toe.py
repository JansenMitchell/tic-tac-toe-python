import tic_tac_toe
import pytest

def test_print_board():
    tic_tac_toe.board = ["-", "-", "-",
                         "-", "-", "-",
                         "-", "-", "-"]
    tic_tac_toe.current_player = "X"
    tic_tac_toe.winner = None
    tic_tac_toe.game_running = True
    tic_tac_toe.print_board()
    assert tic_tac_toe.board == ["-", "-", "-",
                                 "-", "-", "-",
                                 "-", "-", "-"]