
from sudoku import *

# Sample Sudoku
'''
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
'''





count=0

def solve(mat,val):
    global count
    count+=1
    # print("Count: ",val)
    # output_Sudoku(mat)
    for i in range(9):
        for j in range(9):
            if mat[i][j]==0:
                # print("Zero: ",i,j)
                for vals in range(1,10):
                    # print("i,j",i,j,vals)
                    if chkPossible(mat,i,j,vals):
                        # print("Valie: ",vals,i,j)
                        mat[i][j]=vals
                        # print(i,j)
                        res=solve(mat,val+1)
                        if(res == -1):
                            mat[i][j]=0
                            # continue
                        else:
                            mat=res
                            break
                else:
                    return -1
    return mat


output = solve(sudoku2,0)
output_Sudoku(output)
print("Count: ",count)