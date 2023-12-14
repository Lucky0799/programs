def is_safe(board, row, col):
    # Check if there is a queen in the same row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens(board, col + 1):
                return True

            # Backtrack if placing a queen in the current position doesn't lead to a solution
            board[i][col] = 0

    return False

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def four_queens():
    n = 4
    board = [[0] * n for _ in range(n)]

    if solve_queens(board, 0):
        print("Solution found:")
        print_solution(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    four_queens()
