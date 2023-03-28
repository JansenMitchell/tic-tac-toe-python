import tic_tac_toe, pytest

def test_draw_board(capsys):
    tic_tac_toe.draw_board(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    out, err = capsys.readouterr()
    assert out == '-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n'
    
def test_get_player_move(capsys):
    tic_tac_toe.get_player_move([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    # Will only accept numbers 0-8
    out, err = capsys.readouterr()
    assert out == 'Enter your move (0-8): '