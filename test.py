global grid_len
grid_len = 8


def isSafe(mat,row,col):
    for i in range(col): #check for column
        if mat[row][i] == 1:
            return False

    i = row
    j = col

    while(i>=0 and j>=0): #checks for the upper left diagonall
        if(mat[i][j] == 1):
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col

    while(i<grid_len and j>=0): #checks for lower left diagonal
        if(mat[i][j] == 1):
            return False
        i += 1
        j -= 1
    
 
    return True 


def solveQueens(mat,col):

    if col >= grid_len:
        return True

    for i in range(grid_len):
        if isSafe(mat,i,col): # is tile safe
            mat[i][col] = 1
            if(solveQueens(mat,col+1) == True):
                return True
            mat[i][col] = 0
    return False



    
mat = [ [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0] ]
        


    
if(solveQueens(mat,0) == False):
    print("no solution")
else:
    print (mat)



