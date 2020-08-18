pos={0:(0,0),1:(0,3),2:(0,6),3:(3,0),4:(3,3),5:(3,6),6:(6,0),7:(6,3),8:(6,6)}



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

count=0

inp=[[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 0], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]

def chkZero(mat):
    for i in mat:
        if 0 in i:
            return True
    return False

def solve(mat):
    looks=0
    while(chkZero(mat)):
        looks+=1
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
    output_Sudoku(mat)
    print("Looped {} times".format(looks))
solve(inp)
