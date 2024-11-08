#O(n!) and o(n^2)
def is_safe(board,row,col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j] ==1:
            return False    
    for i,j in zip(range(row,len(board)),range(col,-1,-1)):
        if board[i][j] ==1:
            return False   
    return True

def solve_n_queens(board,col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_safe(board,i,col):
            board[i][col] = 1
            if solve_n_queens(board,col+1):
                return True
            board[i][col] = 0
    return False
def print_board(board):
    for row in board:
        print("".join("Q" if col==1 else '.' for col in row))
def solve_8_queens():
    n=8
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[3][0] =1 
    print_board(board)
    if solve_n_queens(board,1):
        print("found soln")
        print_board(board)
    else:
        print("no soln")

if __name__ == "__main__":
    solve_8_queens()