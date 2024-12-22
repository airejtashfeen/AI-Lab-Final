def is_safe(board, row, col):
    for i in range(row):
        if board[i]==col or abs(board[i]-col)== abs(i-row):
            return False
    return True

def solve_n_queens(board, row):
#Backtracking
    if row == len(board):
        # All queens placed
        return True

    for col in range(4): 
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            if solve_n_queens(board, row + 1):  
                return True 
            board[row] = -1  # Backtrack 
    return False  

def print_positions(board):

    for row in range(4):
        print(f"Queen in row {row + 1} is placed in column {board[row] + 1}")

def main():
    board = [-1] * 4  #initialize the board
    if solve_n_queens(board, 0):
        print("Solution found:")
        print_positions(board)
    else:
        print("No solution exists.")

main()
