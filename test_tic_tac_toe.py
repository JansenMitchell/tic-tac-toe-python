import tic_tac_toe, pytest

def test_draw_board(capsys):
    tic_tac_toe.draw_board(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    out, err = capsys.readouterr()
    assert out == '-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n| X | X | X |\n-------------\n'
    
def test_get_player_move():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    tic_tac_toe.get_player_move(board, test_input=0)
    assert board[0] == 'X'

# Test if the AI can win the game    
def test_minimax():
    assert tic_tac_toe.minimax(['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '], 0, True) == -1
    assert tic_tac_toe.minimax([' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' '], 0, True) == -1
    assert tic_tac_toe.minimax([' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X'], 0, True) == -1
    assert tic_tac_toe.minimax(['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' '], 0, True) == -1
    assert tic_tac_toe.minimax([' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' '], 0, True) == -1
    assert tic_tac_toe.minimax([' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X'], 0, True) == -1
    assert tic_tac_toe.minimax(['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'], 0, True) == -1
    assert tic_tac_toe.minimax([' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' '], 0, True) == -1
    assert tic_tac_toe.minimax(['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' '], 0, True) == 1
    assert tic_tac_toe.minimax([' ', ' ', ' ', 'O', 'O', 'O', ' ', ' ', ' '], 0, True) == 1
    assert tic_tac_toe.minimax([' ', ' ', ' ', ' ', ' ', ' ', 'O', 'O', 'O'], 0, True) == 1
    assert tic_tac_toe.minimax(['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' '], 0, True) == 1
    assert tic_tac_toe.minimax([' ', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' '], 0, True) == 1

# Test if the AI move is a valid move    
def test_get_ai_move(): # test that the AI can move
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] # create a board
    tic_tac_toe.get_ai_move(board) # call the AI to make a move
    assert board[0] == 'O' or board[1] == 'O' or board[2] == 'O' or board[3] == 'O' or board[4] == 'O' or board[5] == 'O' or board[6] == 'O' or board[7] == 'O' or board[8] == 'O' # check that the AI made a move
    
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