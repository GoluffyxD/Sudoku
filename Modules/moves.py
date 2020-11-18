from Modules.sudoku import getChoiceMatrix
from Modules.sudoku import pos
# Simple Elimination move
def eliminate_move(mat,possible):
        changed=0
        for i in range(9):
            for j in range(9):
                if len(possible[i][j])==1:
                    mat[i][j]=possible[i][j][0]
                    # possible = getChoiceMatrix(mat)
                    print("Applying basic elimination move")
                    print(f"Looks like {mat[i][j]} is the only number that can be added in {i+1},{j+1}")
                    # output_Sudoku(mat)
                    changed=1
                    return changed
        return changed

# Row Elimination Move
def row_elimination_move(mat,possible):
    changed = 0
    for i in range(9):
        for val in range(1,10):
            count=0
            for k in range(9):
                if val in possible[i][k]:
                    ind=k
                    count+=1
            if count == 1:
                mat[i][ind] = val
                # possible = getChoiceMatrix(mat)
                print("Applying row elimination move")
                print("Looking at the {} row,it seems as though {} is the only number that can be added in {},{}".format(i+1,val,i+1,ind+1))
                changed=1
                return changed
    return changed

# Column Elimination Move
def col_elimination_move(mat,possible):
    changed=0
    for i in range(9):
        for val in range(1,10):
            count=0
            for k in range(9):
                if val in possible[k][i]:
                    ind=k
                    count+=1
            if count == 1:
                mat[ind][i]= val
                # possible = getChoiceMatrix(mat)
                # print("Inserted {} in ({},{}), Column Choice".format(val,ind,i))
                print("Applying column elimination move")
                print(f"Looking at the {i+1} column,it seems as though {val} is the only number that can be added in {ind+1},{i+1}")

                # output_Sudoku(mat)
                changed=1
                return changed
    return changed

def small_square_eliminate_move(mat,possible):
    changed = 0
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
                # possible = getChoiceMatrix(mat)
                # print("Inserted {} in ({},{}), Small Square Choice".format(val,indx,indy))
                print("Applying small square elimination move")
                print("Based on the small square at {},{} seems to be right for {},{}".format(i+1,val,indx+1,indy+1))
                # output_Sudoku(mat)
                changed=1
                return changed
    return changed    
    