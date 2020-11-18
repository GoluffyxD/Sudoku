from Modules.input_output import createSudoku,outputSudoku
from Modules.solve_BruteForce import solve_bruteForce
from Modules.sudoku import getChoiceMatrix,printChoiceMatrix
from Modules.solve_choice import solve_choice
mat = createSudoku("./input_sudoku.txt")
pos = getChoiceMatrix(mat)
# sol,val = solve_bruteForce(mat,0)
# outputSudoku(sol)
# printChoiceMatrix(pos,mat)
sol = solve_choice(mat)
outputSudoku(sol)