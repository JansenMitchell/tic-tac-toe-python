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
        
    def __str__(self):
        return f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} \n---------\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} \n---------\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} \n"