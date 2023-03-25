# Creates the board.
class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        
    def is_empty(self):
        return self.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    
    def is_full(self):
        return not any(" " in row for row in self.board)
    
    def reset(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]