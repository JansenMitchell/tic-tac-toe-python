board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
current_player = "X"
winner = None
game_running = True

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
    
def player_input():
    position = int(input("Choose a position from 1-9: "))
    # Check if the position is valid
    if position >= 1 and position <= 9 and board[position - 1] == "-":
        # If it is, set the position to the current player
        board[position - 1] = current_player
    else:
        print("Invalid position")
        
while game_running:
    print_board()
    player_input()