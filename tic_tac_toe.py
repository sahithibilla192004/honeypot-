# -----------------------------
# Tic Tac Toe Game
# -----------------------------

# Create the board (3x3 grid)
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check if someone has won
def check_winner(symbol):
    # Winning positions (rows, columns, diagonals)
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == symbol:
            return True
    return False

# Main game loop
player = "X"
for turn in range(9):
    print_board()
    print("Player", player, "turn.")
    
    move = int(input("Enter position (1-9): ")) - 1  # user enters 1-9
    if board[move] == " ":
        board[move] = player
    else:
        print("Spot already taken, try again!")
        continue

    # Check winner
    if check_winner(player):
        print_board()
        print("Player", player, "wins!")
        break

    # Switch player
    player = "O" if player == "X" else "X"
else:
    print_board()
    print("It's a draw!")
