def draw_board(board):
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')
    
def get_player_move(board, test_input=None):
    while True:
        try:
            if test_input is not None:
                position = test_input
            else:
                position = int(input('Enter your move (0-8): '))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        if position not in range(9):
            print("Invalid move. Please choose an empty position (0-8).")
        elif board[position] != ' ':
            print("Invalid move. Please choose an empty position (0-8).")
        else:
            board[position] = 'X'
            break
    
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'tie':
        return 0
    # If is_maximizing is True, the AI is trying to maximize its score
    if is_maximizing:
        # Set the best score to the lowest possible value as a starting point,
        # which is -float('inf') or -infinity.
        best_score = -float('inf')
        # Iterate over all possible moves
        for i in range(9):
            # Check if the position is empty
            if board[i] == ' ':
                # Make the move
                board[i] = 'O'
                # Recursively call minimax with is_maximizing set to False to simulate the player's turn
                score = minimax(board, depth + 1, False)
                # Undo the move
                board[i] = ' '
                # Update the best score
                best_score = max(score, best_score)
        return best_score
    else:
        # Set the best score to the highest possible value as a starting point
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                # Recursively call minimax with is_maximizing set to True to simulate the AI's turn
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
    
def get_ai_move(board):
    best_score = -float('inf')
    # Set the best move to the first possible move as a starting point
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            # Recursively call minimax with is_maximizing set to False to simulate the player's turn
            score = minimax(board, 0, False)
            board[i] = ' '
            # Update the best score and best move
            if score > best_score:
                best_score = score
                best_move = i
    # Make the move
    board[best_move] = 'O'

    
def check_winner(board):
    # Check all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    # Iterate over all possible winning combinations
    for combo in winning_combinations:
        # Check if the first, second, and third positions in the winning combination are equal
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    # If there are no more empty spaces, the game ends in a tie
    if ' ' not in board:
        return 'tie'
    # If no one has won yet, return None
    return None

def game_loop():
    board = [' '] * 9
    while True:
        draw_board(board)
        get_player_move(board)
        if check_winner(board):
            break
        get_ai_move(board)
        if check_winner(board):
            break
    draw_board(board)
    if check_winner(board) == 'tie':
        print('Tie!')
    else:
        print(check_winner(board) + ' wins!')

game_loop()