def is_safe(board,row,col):
    for i in range(len(board)):
        if board[i][col]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,len(board))):
        if board[i][j]==1:
            return False
    return True
def solve(board,row):
    if row>=len(board):
        return True
    for col in range(len(board)):
        if is_safe(board,row,col):
            board[row][col]=1
            if solve(board,row+1):
                return True
            board[row][col]=0
    return False
def print_list(board):
    for row in board:
        print(row)
def eight_queens(n):
    board=[[0]*n for i in range(n)]
    if solve(board,0):
        print_list(board)
    else:
        print("No Solution")
eight_queens(4)