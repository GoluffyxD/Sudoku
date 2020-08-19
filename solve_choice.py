from sudoku import *

count=0

def solve_choice(mat):
    looks=0
    possible = getChoiceMatrix(mat)
    changed=1
    while chkZero(mat):

        print(looks)
        looks+=1
        changed=0
        # Check Elimination
        for i in range(9):
            for j in range(9):
                if len(possible[i][j])==1:
                    mat[i][j]=possible[i][j][0]
                    possible = getChoiceMatrix(mat)
                    print("Inserted {} to ({},{}), Elimination Choice".format(mat[i][j],i,j))
                    output_Sudoku(mat)
                    changed=1
        # Check Row Combination
        for i in range(9):
            # print('Row: ',i,possible[i])
            for val in range(1,10):
                count=0
                for k in range(9):
                    if val in possible[i][k]:
                        ind=k
                        count+=1
                if count == 1:
                    mat[i][ind] = val
                    # print("Val: ",val)
                    # print("Changed",i,possible[i])
                    possible = getChoiceMatrix(mat)
                    # print("Changed",i,possible[i])
                    print("Inserted {} in ({},{}), Row Choice".format(val,i,ind))
                    output_Sudoku(mat)
                    changed=1
        
        # Check Column Combination
        for i in range(9):
            for val in range(1,10):
                count=0
                for k in range(9):
                    if val in possible[k][i]:
                        ind=k
                        count+=1
                if count == 1:
                    mat[ind][i]= val
                    possible = getChoiceMatrix(mat)
                    print("Inserted {} in ({},{}), Column Choice".format(val,ind,i))
                    output_Sudoku(mat)
                    changed=1

        # Check Small Squares
        for i in range(9):
            (startx,starty) = pos[i]
            for val in range(1,10):
                count=0
                for k in range(startx,startx+3):
                    for l in range(starty,starty+3):
                        if val in possible[k][l]:
                            count+=1
                            indx=k
                            indy=l
                if count == 1:
                    mat[indx][indy] = val
                    possible = getChoiceMatrix(mat)
                    print("Inserted {} in ({},{}), Small Square Choice".format(val,indx,indy))
                    output_Sudoku(mat)
                    changed=1
        # break
        if changed == 0:
            print("Stuck")
            output_Sudoku(mat)
            possible = getChoiceMatrix(mat)
            printChoiceMatrix(possible,mat)
            return possible,mat
    return possible,mat
            # break
    # output_Sudoku(mat)
print("Input")
output_Sudoku(sudoku1)
print("Choices")
# possible = getChoiceMatrix(sudoku2)
# printChoiceMatrix(possible,sudoku2)
op_possible,op_mat = solve_choice(sudoku1)
output_Sudoku(op_mat)
# red_possible = reduceChoiceMatrix(op_possible)
# print("Reduced Matrix")
# printChoiceMatrix(red_possible,op_mat)