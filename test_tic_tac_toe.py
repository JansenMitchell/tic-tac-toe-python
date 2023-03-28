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

# Test if the AI move is a valid move    
def test_get_ai_move():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    tic_tac_toe.get_ai_move(board)
    assert board[0] == 'O' or board[1] == 'O' or board[2] == 'O' or board[3] == 'O' or board[4] == 'O' or board[5] == 'O' or board[6] == 'O' or board[7] == 'O' or board[8] == 'O'
    
def test_check_winner():
    assert tic_tac_toe.check_winner(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']) == 'X'
    assert tic_tac_toe.check_winner([' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']) == 'X'
    assert tic_tac_toe.check_winner([' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']) == 'X'
    assert tic_tac_toe.check_winner(['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']) == 'X'
    assert tic_tac_toe.check_winner([' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']) == 'X'
    assert tic_tac_toe.check_winner([' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']) == 'X'
    assert tic_tac_toe.check_winner(['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']) == 'X'
    assert tic_tac_toe.check_winner([' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']) == 'X'
    assert tic_tac_toe.check_winner(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']) == 'O'
    assert tic_tac_toe.check_winner([' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' ']) == 'O'
    assert tic_tac_toe.check_winner([' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O']) == 'O'
    assert tic_tac_toe.check_winner(['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']) == 'O'
    assert tic_tac_toe.check_winner([' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' ']) == 'O'
    assert tic_tac_toe.check_winner([' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O']) == 'O'
    assert tic_tac_toe.check_winner(['O', ' ', ' ', ' ', 'O', ' ', ' ', ' ', 'O']) == 'O'
    
# Test if game is running. If it is, it will return True
def test_game_loop():
    assert tic_tac_toe.game_loop() == True