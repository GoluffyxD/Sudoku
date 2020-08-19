from sudoku import *

count=0








def solve(mat):
    looks=0
    while(chkZero(mat)):
        looks+=1
        print(looks)
        for i in range(9):
            for j in range(9):
                if mat[i][j]==0:
                    valcount=0
                    for vals in range(1,10):
                        if chkPossible(mat,i,j,vals):
                            valcount+=1
                            inval=vals
                    if valcount==1:
                        mat[i][j]=inval
                        print("Inserted {} in ({},{})".format(inval,i,j))
        
        # Check for combinations in row
        for i in range(9):
            row=[]
            for j in range(9):
                if mat[i][j]==0:
                    row.append([vals for vals in range(1,10) if chkPossible(mat,i,j,vals)])
                else:
                    row.append([])
            for el in range(1,10):
                count=0
                for k in range(9):
                    if el in row[k]:
                        ind=k
                        count+=1
                if count == 1:
                    mat[i][ind]==el
                    print("Inserted {} in ({},{})".format(el,i,ind))
        
        # Check for combination in column
        for i in range(9):
            col=[]
            for j in range(9):
                if mat[j][i] == 0:
                    col.append([vals for vals in range(1,10) if chkPossible(mat,j,i,vals)])
                else:
                    col.append([])
            for el in range(1,10):
                count=0
                for k in range(9):
                    if el in col[k]:
                        ind=k
                        count+=1
                if count == 1:
                    mat[ind][i]==el
                    print("Inserted {} in ({},{})".format(el,ind,i))
        
        # Check for Combination in Small Square
        for i in range(9):
            (startx,starty) = pos[i]
            box=[]
            for k in range(startx,startx+3):
                temp=[]
                for l in range(starty,starty+3):
                    if mat[k][l] == 0:
                        temp.append([vals for vals in range(1,10) if chkPossible(mat,k,l,vals)])
                    else:
                        temp.append([])
                box.append(temp)
            for el in range(1,10):
                count=0
                for k in range(3):
                    for l in range(3):
                        if el in box[k][l]:
                            count+=1
                            indx=k
                            indy=l
                if count == 1:
                    mat[indx][indy]==el
                    print("Inserted {} in ({},{})".format(el,indx,indy))

    output_Sudoku(mat)
    print("Looped {} times".format(looks))

def solve_choice(mat):
    looks=0
    possible = getChoiceMatrix(mat)
    changed=1
    while chkZero(mat):

        print(looks)
        looks+=1
        changed=0
        # Take obvious Choice
        for i in range(9):
            for j in range(9):
                if len(possible[i][j])==1:
                    mat[i][j]=possible[i][j][0]
                    possible = getChoiceMatrix(mat)
                    print("Inserted {} to ({},{}), Elimination Choice".format(mat[i][j],i,j))
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
                    changed=1
        # break
        if changed == 0:
            print("Stuck")
            output_Sudoku(mat)
            possible = getChoiceMatrix(mat)
            printChoiceMatrix(possible,mat)
            break
    # output_Sudoku(mat)

possible = getChoiceMatrix(sudoku2)
printChoiceMatrix(possible,sudoku2)
solve_choice(sudoku2)