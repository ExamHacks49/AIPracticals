def solveNQueen(n):
    col = set()
    pos_diag = set()
    neg_diag = set()

    result = []
    board = [['.'] * n for _ in range(n)]

    def bactrack(row):
        if row == n:
            board_copy = ["".join(row) for row in board]
            result.append(board_copy)
            return

        for column in range(n):
            if column in col or (row + column) in pos_diag or (row - column) in neg_diag:
                continue

            col.add(column)
            pos_diag.add(row + column)
            neg_diag.add(row - column)
            board[row][column] = 'Q'

            bactrack(row + 1)

            col.remove(column)
            pos_diag.remove(row + column)
            neg_diag.remove(row - column)
            board[row][column] = '.'
    bactrack(0)
    return result
def print_board(solution):
    i = 1
    for col in solution:
        print(f"\n\nSolution {i}")
        for string in col:
            print(string)
        i+=1
            
n = int(input("Enter the number of slots in the chess board: "))
solution = solveNQueen(n)
print(f'Number of solutions: {len(solution)}')
print_board(solution)