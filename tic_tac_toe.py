# a simple Tic Tac Toe program that satisfies the following requirements:
# It must have a UI so that I can play.  A console UI will do just fine.
# The program must play fair Tic Tac Toe against me
# The program must be unbeatable, and win every chance I give it

import random

# Board class
class Board:
    # Initializes the board with a list of 9 zeros.
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def display(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])

    # Updates the board with the player's move.
    def update(self, position, player):
        # Checks if the position is empty.
        self.board[position] = player

    def check_win(self, player):
        # Check rows
        if self.board[0] == player and self.board[1] == player and self.board[2] == player:
            return True
        if self.board[3] == player and self.board[4] == player and self.board[5] == player:
            return True
        if self.board[6] == player and self.board[7] == player and self.board[8] == player:
            return True
        # Check columns
        if self.board[0] == player and self.board[3] == player and self.board[6] == player:
            return True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        # Check diagonals
        if self.board[0] == player and self.board[4] == player and self.board[8] == player:
            return True
        if self.board[2] == player and self.board[4] == player and self.board[6] == player:
            return True
        return False

    def check_draw(self):
        for i in range(9):
            # If the board has an empty position, return False.
            if self.board[i] == 0:
                return False
        # Returns True if the board has no winning row, column, or diagonal.
        return True

    def check_game_over(self, player):
        if self.check_win(player) or self.check_draw():
            return True
        return False

# Resets the board to a new game.
    def reset(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]