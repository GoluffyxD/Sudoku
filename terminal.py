from Modules.input_output import createSudoku,outputSudoku
from Modules.solve_BruteForce import solve_bruteForce
from Modules.sudoku import getChoiceMatrix,printChoiceMatrix,chkZero
from Modules.solve_choice import solve_choice
PATH = "./input_sudoku.txt"
mat = createSudoku(PATH)
pos = getChoiceMatrix(mat)
sol = solve_choice(mat)
outputSudoku(sol)
if chkZero(sol):
    print("Stuck! Cannot decide next move")