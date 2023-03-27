import random

def draw_board(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    
def is_space_free(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def get_player_move(board):
    while True:
        print('What is your next move? (1-9)')
        move = input()
        if move in '1 2 3 4 5 6 7 8 9'.split() and is_space_free(board, int(move)):
            return int(move)
        else:
            print('That is not a valid move. Choose again.')