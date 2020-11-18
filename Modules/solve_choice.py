from Modules.input_output import outputSudoku
from Modules.sudoku import getChoiceMatrix,printChoiceMatrix,chkZero
from Modules.moves import eliminate_move,row_elimination_move,col_elimination_move,small_square_eliminate_move

def solve_choice(mat):
    looks=0
    possible = getChoiceMatrix(mat)
    while chkZero(mat):
        print(looks)
        # possible = getChoiceMatrix(mat)
        looks+=1
        changed=0
        # Check Elimination
        changed = eliminate_move(mat,possible)
        if changed:
            possible = getChoiceMatrix(mat)
            continue
        # Check Row Combination
        changed = row_elimination_move(mat,possible)
        if changed:
            possible = getChoiceMatrix(mat)
            continue
        # Check Column Combination
        changed = col_elimination_move(mat,possible)
        if changed:
            possible = getChoiceMatrix(mat)
            continue
        # Check Small Squares
        changed = small_square_eliminate_move(mat,possible)
        if changed:
            possible = getChoiceMatrix(mat)
            continue
        if changed == 0:
            print("Hmmm I'm Stuck")
            outputSudoku(mat)
            possible = getChoiceMatrix(mat)
            printChoiceMatrix(possible,mat)
            return mat
    return mat

