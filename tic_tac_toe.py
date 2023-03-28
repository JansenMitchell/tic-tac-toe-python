import random

def draw_board(board):
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    
def get_player_move(board):
    while True:
        try:
            position = int(input('Enter your move (0-8): '))
            if position not in range(9):
                raise ValueError
            if board[position] != ' ':
                raise ValueError
            break
        except ValueError:
            print('Invalid move. Please choose an empty position (0-8).')
    board[position] = 'X'
    
def get_ai_move(board):
    position = random.choice([i for i in range(9) if board[i] == ' '])
    board[position] = 'O'
    
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'tie'
    return None

def game_loop():
    board = [' '] * 9
    while True:
        draw_board(board)
        get_player_move(board)
        if check_winner(board):
            break
        get_ai_move(board)
        if check_winner(board):
            break
    draw_board(board)
    if check_winner(board) == 'tie':
        print('Tie!')
    else:
        print(check_winner(board) + ' wins!')
        
game_loop()