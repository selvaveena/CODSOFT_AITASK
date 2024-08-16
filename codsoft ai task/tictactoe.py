import random
# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False
def is_full(board):
    return all(cell != " " for row in board for cell in row)
# Function to get available moves on the board
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
# Function for the Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "O"
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for move in available_moves(board):
            board[move[0]][move[1]] = "X"
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            min_eval = min(min_eval, eval)
        return min_eval
    # Function to find the best move for the AI
def best_move(board):
    best_val = float("-inf")
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = "O"
        move_val = minimax(board, 0, False)
        board[move[0]][move[1]] = " "
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move
# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are 'X', and the AI is 'O'.")
    print("Valid Entries: 0 0, 0 1, 0 2, 1 0, 1 1, 1 2, 2 0, 2 1 2 2")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row and column, e.g., '1 2'): ").split())
        if (row, col) not in available_moves(board):
            print("Invalid move. Try again.")
            continue
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win! Congratulations!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"
        print("AI's move:")
        print_board(board)

        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

        if is_full(board):
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    main()