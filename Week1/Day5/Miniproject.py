def display_board(board):
    # We draw the game grid

    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    



def player_input(board, player):
    while True:
     row = int(input(f"Player {player}, enter a line (1-3) : ")) - 1
     column = int(input(f"Player {player}, enter a column (1-3) : ")) - 1
     if 0 <= row < 3 and 0 <= column < 3:  # we check that the indices are valid going from index 0 to index 8

                index = row * 3 + column  # calculation of the grid index which must be between 0 and 8

                if board[index] == " ":
                    board[index] = player  # Place "X" or "O"
                    break
                else:
                    print(" This square is already taken, try again.")

def check_win(board):
    
    # We then make a list of the winning combinations depending of the index
    winning_combinations = [
        (0, 1, 2),  # Line 1
        (3, 4, 5),  # Line 2
        (6, 7, 8),  # Line 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal 1
        (2, 4, 6)   # Diagonal 2
    ]
    
    # We check each winning combination

    for (x, y, z) in winning_combinations:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return board[x]  # Return "X" or "O" if a winner is found

    
    # We check if there is a Tie
    if " " not in board:
        return "Tie"  # Return "Tie" if all boxes are filled
    
    return None  #  No winner, game continues


def play():
    
    board = [" "] * 9  # Creates an empty grid of 9 squares
    player = "X"  # Player X starts
    
    while True:
        display_board(board)  
        player_input(board, player)  
        
        
        result = check_win(board)
        if result:
            display_board(board)  # show final grid
            if result == "Tie":
                print("It's a tie !")
            else:
                print(f" The player {result} won ! ")
            break  # Game ends if a winner or a draw
        
        # player change 
        player = "O" if player == "X" else "X"

# Start the game
play()