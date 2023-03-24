import random

class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        
    def draw(self):
        print(' {} | {} | {} '.format(self.board[0], self.board[1], self.board[2]))
        print('-----------')
        print(' {} | {} | {} '.format(self.board[3], self.board[4], self.board[5]))
        print('-----------')
        print(' {} | {} | {} '.format(self.board[6], self.board[7], self.board[8]))
    
    def update(self, position, player):
        self.board[position] = player
        
    def is_empty(self, position):
        return self.board[position] == ' '
    
    def is_full(self):
        return ' ' not in self.board
    
    def reset(self):
        self.board = [' ' for _ in range(9)]
        
# TODO: Player class

# TODO: AI class

# TODO: Game class
