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
        
class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
        
    def get_move(self, board):
        pass
    
# TODO: Human Player class
class HumanPlayer(Player):
    def __init__(self, name, marker):
        super().__init__(name, marker)
        
    def get_move(self, board):
        while True:
            position = input('Enter a position (0-8): ')
            if position.isdigit() and board.is_empty(int(position)):
                return int(position)
            else:
                print('Invalid move. Try again.')

# TODO: AI Player class

# TODO: Game class
