# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Conditionals (if, elif, else)
# Loops (for, while)
# Functions
# List manipulation
# User input

# Key Python Topics:
# Lists (2D lists)
# Loops (while)
# Conditional statements (if, elif, else)
# Functions
# User input (input())
# String formatting

# 🛠️ What you will create
# A command-line Tic Tac Toe game that allows two players to take turns marking a 3x3 grid.

# Instructions:
# Tic Tac Toe is played on a 3x3 grid. Players take turns marking empty squares with their symbol (‘O’ or ‘X’). The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins. If all squares are filled and no player has three in a row, the game is a tie.

# Step 1: Representing the Game Board
# You’ll need a way to represent the 3x3 grid.
# A list of lists (a 2D list) is a good choice.
# Initially, each cell in the grid should be empty (e.g., represented by a space ‘ ‘).

# Step 2: Displaying the Game Board
# Create a function called display_board() to print the current state of the game board.
# The output should visually represent the 3x3 grid.
# Think about how to format the output to make it easy to read.

# Step 3: Getting Player Input
# Create a function called player_input(player) to get the player’s move.
# The function should ask the player to enter a position (e.g., row and column numbers).
# Validate the input to ensure it’s within the valid range and that the chosen cell is empty.
# Think about how to ask the user for input, and how to validate that input.

# Step 4: Checking for a Winner
# Create a function called check_win(board, player) to check if the current player has won.
# The function should check all possible winning combinations (rows, columns, diagonals).
# If a player has won, return True; otherwise, return False.
# Think about how to check every possible winning combination.

# Step 5: Checking for a Tie
# Create a function to check if the game has resulted in a tie.
# The function should check if all positions of the board are full, without a winner.

# Step 6: The Main Game Loop
# Create a function called play() to manage the game flow.
# Initialize the game board.
# Use a while loop to continue the game until there’s a winner or a tie.
# Inside the loop:
# Display the board.
# Get the current player’s input.
# Update the board with the player’s move.
# Check for a winner.
# Check for a tie.
# Switch to the next player.
# After the loop ends, display the final result (winner or tie).

# Tips:
# Consider creating helper functions to break down the logic into smaller, manageable parts.
# Follow the single responsibility principle: each function should do one thing and do it well.
# Think about how to switch between players.
# Think about how you will store the player’s symbol.

# ****************************************
# *********** global variables ***********
# ****************************************

board = [['','',''] for i in range(3)]   # Global board variable

# ****************************************
# *********** helper functions ***********
# ****************************************

def get_coordinate(axis: str) -> int:
    """get either row or column (axis) value from user\n
    and return its value"""
    while True:
        index = input(f"Enter {axis} number: ")
        if index.isdigit() and int(index) in range(1, 4):   # check if index is integer and if it is in the correct range
            return int(index) - 1
        else:
            print("Invalid choice: must be an integer between 1 and 3 (inclusive).")

def check_rows(board: list, player: str) -> bool:
    """check if there are any rows with the same player\n
    if there are, return True, False otherwise"""
    for i in range(3):  # for each line
        if all(cell == player for cell in board[i]):    # check if every entry in the line has the same player
            return True
    return False

def check_columns(board:list, player: str) -> bool:
    """check if there are any columns with the same player\n
    if there are, return True, False otherwise"""
    for j in range(3): # for each column
        if all(board[i][j] == player for i in range(3)):    # check if every entry in the column has the same player
            return True
    return False

def check_diagonals(board:list, player: str) -> bool:
    """check if there are any diagonals with the same player\n
    if there are, return True, False otherwise"""
    if all(board[i][i] == player for i in range(3)):    # check if main diagonal has the same player
        return True
    elif all(board[i][2 - i] == player for i in range(3)):  # check if the secondary diagonal has the same player
        return True
    else:
        return False

# *********************************************
# *********** main/public functions ***********
# *********************************************

def display_board(board: list) -> None:
    """Print the current game board"""
    print("TIC-TAC-TOE")
    print("*****************")
    for i in range(3):
        print("*  ", end="")
        for j in range(3):
            if board[i][j] == "":
                print("   ", end="")
            elif board[i][j] == "X":
                print(" X ", end="")
            else:
                print(" O ", end="")
            if j < 2:
                print("|", end="")
        print("  *")
        if i < 2:
            print("*  ---|---|---  *")
    print("*****************")

def player_input(player: str) -> None:
    """get the player moves and update the board"""
    while True:
        row = get_coordinate("row")         # player chose row value
        column = get_coordinate("column")   # player chose column value
        if board[row][column] == "":        # check if cell is occupied
            board[row][column] = player     # if so, update cell
            print("Play board updated!")
            break
        else:
            print("This cell is already chosen, please choose another cell.")

def check_win(board: list, player: str) -> bool:
    """Check if the player won the game.\n
    if so, return True, otherwise return False"""
    row_win = check_rows(board, player)         # check if player won any rows
    column_win = check_columns(board, player)   # check if player won any columns
    diagonal_win = check_diagonals(board, player)   # check if player won any diagonal
    if row_win or column_win or diagonal_win:   # if any of those cases are true
        return True
    else:
        return False

def check_tie(board:list) -> bool:
    """Check if there is a tie.\n
    is so return True; otherwise, return False"""
    if all(board[i][j] != "" for i in range(3) for j in range(3)):  # check if every cell is occupied
        return True
    else:
        return False

def update_player(player: str) -> str:
    """Switch to the next player"""
    if player == "X":
        return "O"
    else:
        return "X"
    
def play():
    player = "X"                            # initialize player variable

    print("Welcome to Tic-Tac-Toe!")
    print()

    while True:
        display_board(board)
        print()

        print(f"Player {player}'s turn ...")
        player_input(player)
        if check_win(board, player):
            print(f"Player {player} won the game!")
            print()
            print("Thanks for playing!")
            break
        elif check_tie(board):
            print("That's a tie!")
            print()
            print("Thanks for playing!")
            break
        else:
            player = update_player(player)


play()
    