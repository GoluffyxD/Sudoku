from Modules.solve_BruteForce import solve_bruteForce
from Modules.input_output import createSudoku
from Modules.sudoku import chkZero 
mat = createSudoku("./input_sudoku.txt")

sol,val  = solve_bruteForce(mat,0)

if chkZero(sol):
    print("Impossible Sudoku. Ambigious choices present.")
else:
    print("The input Sudoku is a Proper Sudoku and can be solved")