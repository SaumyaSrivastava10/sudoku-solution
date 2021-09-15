#!/usr/bin/python3


def blank(puzzle):
    # To find the blank spaces we go through each element in it
    for row in range(9):
        # row = 1,2,3,4,5...9
        for col in range(9):
            # column = 1,2,3,4,5...9
            if puzzle[row][col]==-1:
                # return row and column with blank space
                return row,col
    # Indicate that there are no spaces
    return None,None
def valid(guess,puzzle,row,column):
    rowelements=puzzle[row]
    if guess in rowelements:
        return False
    celements=[puzzle[i][column] for i in range(9)]
    if guess in celements:
        return False
    r=(row//3)*3
    c=(column//3)*3
    for i in range(r,r+3):
        for j in range(c,c+3):
            if puzzle[i][j]==guess:
                return False
    return True
def solve(puzzle):
    #To find the blank spaces in sudoku
    r,c= blank(puzzle)

    if r==None:
        return True
    else:
        for guess in range(1,10):
            if valid(guess,puzzle,r,c)==True:
                puzzle[r][c]=guess

                if solve(puzzle):
                    return True
            puzzle[r][c]=-1
        return False
        solve(puzzle)

if __name__=="__main__":
    arr=[[-1,-1,-1,6,-1,-1,4,-1,-1],
        [7,-1,-1,-1,-1,3,6,-1,-1],
        [-1,-1,-1,-1,9,1,-1,8,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
        [-1,5,-1,1,8,-1,-1,-1,3],
        [-1,-1,-1,3,-1,6,-1,4,5],
        [-1,4,-1,2,-1,-1,-1,6,-1],
        [9,-1,3,-1,-1,-1,-1,-1,-1],
        [-1,2,-1,-1,-1,-1,1,-1,-1]]
    solve(arr)
    print(arr)
