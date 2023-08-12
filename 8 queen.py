def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
    # without attacking any other queen

    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper diagonal on the left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper diagonal on the right side
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_queen_problem(board, row):
    # Base case: If all queens are placed, return True
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            # Recursive call to place the next queen
            if solve_queen_problem(board, row + 1):
                return True
            board[row][col] = 0

    # No safe position found for the current queen
    return False


def eight_queen_problem():
    # Initialize an 8x8 chessboard with zeros
    board = [[0 for _ in range(8)] for _ in range(8)]

    # If a solution exists, print the board
    if solve_queen_problem(board, 0):
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    eight_queen_problem()
