# a simple Tic Tac Toe program that satisfies the following requirements:
# It must have a UI so that I can play.  A console UI will do just fine.
# The program must play fair Tic Tac Toe against me
# The program must be unbeatable, and win every chance I give it

# Required imports
import random

# TODO: Board class
# This class can have methods to initialize the board
# and take in a move and mark it on the board.
class Board:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def mark(self, move, mark):
        # Assigns the mark to the board at the move index
        self.board[move - 1] = mark
    
# TODO: Player class
# This class can have methods to get the player’s move and mark on the board.

# TODO: AI class
# Use the minimax algorithm to determine the best move for the AI

# TODO: Game class
# This class can have methods to initialize the game, 
# get the current player, get the next move, and check if the game is over.