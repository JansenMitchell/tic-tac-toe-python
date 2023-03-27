import tic_tac_toe, pytest

def test_draw_board(capsys):
    tic_tac_toe.draw_board(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    out, err = capsys.readouterr()
    assert out == '-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n'