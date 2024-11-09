# Importing the required module to clear the console screen
import os

# Function to initialize the board
def initialize_board():
    # The board is a list of 9 elements representing each cell, initially empty
    return [' ' for _ in range(9)]

# Function to print the current board
def print_board(board):
    # Printing the board in a 3x3 grid format
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen (Windows or Unix-based)
    print("Tic Tac Toe\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check if a player has won
def check_winner(board, player):
    # All possible winning combinations of indices on the board
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontals
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Verticals
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    
    # Check if any winning combination has all the same symbol (player's symbol)
    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function to check if the board is full (no empty spaces left)
def is_board_full(board):
    return ' ' not in board

# Function to play the game
def play_game():
    # Initialize the board and set the first player to 'X'
    board = initialize_board()
    current_player = 'X'
    
    # Main game loop: continue until the game is over
    while True:
        print_board(board)  # Print the current state of the board
        
        # Ask the current player to choose a position (1-9)
        try:
            position = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        # Check if the position is valid (between 0 and 8) and the cell is not already taken
        if position < 0 or position > 8 or board[position] != ' ':
            print("Invalid move! The position is either out of range or already occupied.")
            continue
        
        # Place the current player's symbol on the board
        board[position] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (draw condition)
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch the player
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
if __name__ == "__main__":
    play_game()
