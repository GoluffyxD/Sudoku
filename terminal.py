from Modules.input_output import createSudoku,outputSudoku
from Modules.solve_BruteForce import solve_bruteForce
from Modules.sudoku import getChoiceMatrix,printChoiceMatrix
from solve_choice import solve_choice
mat = createSudoku("./input_sudoku.txt")
pos = getChoiceMatrix(mat)
printChoiceMatrix(pos,mat)
sol,pos = solve_choice(mat)
outputSudoku(sol)