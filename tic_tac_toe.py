# Creates the board.
class Board:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        
    def is_empty(self):
        return self.board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]