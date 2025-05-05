#!/usr/bin/python3

def print_board(board):
    """Prints the current game board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Checks if there is a winner on the board."""
    # Check horizontal rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check vertical columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def valid_input(board):
    """Validates user input for row and column."""
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input! Please enter numbers for row and column.")
            
def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    # Keep playing until there's a winner
    while not check_winner(board):
        print_board(board)
        print(f"Player {player}'s turn:")
        
        # Get valid row and column input
        row, col = valid_input(board)
        
        # Make the move
        board[row][col] = player
        
        # Check if the game is won
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return
        
        # Switch player
        player = "O" if player == "X" else "X"
    
    print_board(board)
    print("It's a draw!")

# Start the game
tic_tac_toe()
