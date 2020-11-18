from Modules.sudoku import chkPossible
import copy

def solve_bruteForce(mat_parameter,val):
    mat = copy.deepcopy(mat_parameter)
    for row in range(9):
        for col in range(9):
            if mat[row][col]==0:
                for vals in range(1,10):
                    if chkPossible(mat,row,col,vals):
                        mat[row][col]=vals
                        res,val=solve_bruteForce(mat,val+1)
                        if(res == -1):
                            mat[row][col]=0
                            val=val-1
                        else:
                            mat=res
                            break
                else:
                    return -1,val
    # print(val)
    return mat,val