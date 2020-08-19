


pos={0:(0,0),1:(0,3),2:(0,6),3:(3,0),4:(3,3),5:(3,6),6:(6,0),7:(6,3),8:(6,6)}
sudoku1=[[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 0], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]
sudoku2 =[[0,0,7,0,0,0,0,0,4],[0,0,0,6,5,0,0,0,2],[0,2,0,8,0,1,0,6,0],[0,1,0,0,0,0,0,0,0],[0,0,0,0,4,0,7,8,5],[5,0,2,0,0,0,0,0,0]
,[1,0,0,0,0,0,0,0,0],[0,9,4,0,0,0,0,0,0],[0,0,0,9,2,0,0,0,6]]

def input_Sudoku():
    mat=[]
    print("Input Sudoku: ")
    for i in range(9):
        l=[int(i) for i in input().split()]
        mat.append(l)
    return mat

def output_Sudoku(mat):
    print("Output: ")
    for i in mat:
        print(*i)

def chkPossible(mat,x,y,val):
    if val in mat[x][:]:
        # print("Failed Row")
        return False
    if val in [temp[y] for temp in mat ]:
        # print(mat[:][y])
        # print("Failed Col")
        return False
    posKey= 3*(x//3) + y//3
    (startx,starty)=pos[posKey]
    for i in range(startx,startx+3):
        for j in range(starty,starty+3):
            if mat[i][j]== val:
                return False
    return True

def getChoiceMatrix(mat):
    possible=[]
    for i in range(9):
        temp=[]
        for j in range(9):
            if mat[i][j]==0:
                temp.append([vals for vals in range(1,10) if chkPossible(mat,i,j,vals)])
            else:
                temp.append([])
        possible.append(temp)
    while possible!= reduceChoiceMatrix(possible):
        possible = reduceChoiceMatrix(possible)
    return possible

def chkZero(mat):
    for i in mat:
        if 0 in i:
            return True
    return False

def printChoiceMatrix(possible,mat):
    for i in range(9):
        for j in range(9):
            if possible[i][j]==[]:
                print(mat[i][j],'\t',end='')
            else:
                str1='c'
                for val in possible[i][j]:
                    str1+=str(val)
                # print('(',end='')
                # for el in possible[i][j]:
                    # print(el,',',end='')
                # print(')',end='')
                print(str1,'\t',end='')
                # print('\t',end='')
            print('|',end='')
        print('\n')

def reduceChoiceMatrix(possible):
    #Row Reduce
    # temp = possib#le.copy()
    for i in range(9):
        for j in range(9):
            if possible[i][j] in possible[i][j+1:]:
                val = possible[i][j]
                for k in range(9):
                    if len(possible[i][k])>len(val):
                        for el in val:
                            if el in possible[i][k]:
                                try:
                                    possible[i][k].remove(el)
                                except:
                                    pass
    
    # Column Reduce
    for i in range(9):
        freq={}
        for j in range(9):
            if tuple(possible[j][i]) in freq.keys():
                freq[tuple(possible[j][i])]+=1
            else:
                freq[tuple(possible[j][i])]=1
        for el in freq.keys():
            if freq[el]>1 and el!=():
                for m in range(9):
                    if len(possible[m][i])>len(el):
                        for val in el:
                            if val in possible[m][i]:
                                try:
                                    possible[m][i].remove(val)
                                except:
                                    pass
    
    # Small Square Reduce
    for i in range(9):
        (startx,starty)=pos[i]
        freq={}
        for k in range(startx,startx+3):
            for l in range(starty,starty+3):
                if tuple(possible[k][l]) in freq.keys():
                    freq[tuple(possible[k][l])]+=1
                else:
                    freq[tuple(possible[k][l])]=1
        for el in freq.keys():
            if freq[el]>1 and el!=():
                for k in range(startx,startx+3):
                    for l in range(starty,starty+3):
                        if len(possible[k][l])>len(el):
                            for val in el:
                                if val in possible[k][l]:
                                    try:
                                        possible[k][l].remove(val)
                                    except:
                                        pass
    
    return possible
