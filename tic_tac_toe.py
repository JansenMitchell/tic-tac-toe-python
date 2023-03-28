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