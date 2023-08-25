def isSafe(mat, r, c):
    for i in range(r):      # checking in that column
        if mat[i][c] == 'Q':
            return False
    (i, j) = (r, c)
    while i >= 0 and j >= 0:   # diagonal 1
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
    (i, j) = (r, c)
    while i >= 0 and j < len(mat):    # diagonal 2 
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
    return True

def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
    print()

def nQueen(mat, r):
    if r == len(mat):
        printSolution(mat)
        return
    for i in range(len(mat)):
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'
            nQueen(mat, r + 1)
            mat[r][i] = '-'
            
N=int(input("Enter value of n:"))
mat = [['-' for x in range(N)] for y in range(N)]
nQueen(mat, 0)
