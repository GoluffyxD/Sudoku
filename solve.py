# Sample Sudoku
'''
0 0 0 2 6 0 7 0 1
6 8 0 0 7 0 0 9 0
1 9 0 0 0 4 5 0 0
8 2 0 1 0 0 0 4 0
0 0 4 6 0 2 9 0 0
0 5 0 0 0 3 0 2 8
0 0 9 3 0 0 0 7 4
0 4 0 0 5 0 0 3 6
7 0 3 0 1 8 0 0 0
'''
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

def solve(mat,val):
    global count
    count+=1
    # print("Count: ",val)
    # output_Sudoku(mat)
    for i in range(9):
        for j in range(9):
            if mat[i][j]==0:
                # print("Zero: ",i,j)
                for vals in range(1,10):
                    # print("i,j",i,j,vals)
                    if chkPossible(mat,i,j,vals):
                        # print("Valie: ",vals,i,j)
                        mat[i][j]=vals
                        # print(i,j)
                        res=solve(mat,val+1)
                        if(res == -1):
                            mat[i][j]=0
                            # continue
                        else:
                            mat=res
                            break
                else:
                    return -1
    return mat

inp=[[0, 0, 0, 2, 6, 0, 7, 0, 1], [6, 8, 0, 0, 7, 0, 0, 9, 0], [1, 9, 0, 0, 0, 4, 5, 0, 0], [8, 2, 0, 1, 0, 0, 0, 4, 0], [0, 0, 4, 6, 0, 2, 9, 0, 0], [0, 5, 0, 0, 0, 3, 0, 2, 8], [0, 0, 9, 3, 0, 0, 0, 7, 4], [0, 4, 0, 0, 5, 0, 0, 3, 6], [7, 0, 3, 0, 1, 8, 0, 0, 0]]
# inp=input_Sudoku()
# print(inp)
# output_Sudoku(inp)
# print(chkPossible(inp,0,5,9))
# print(inp[:][0])

output = solve(inp,0)
output_Sudoku(output)
print("Count: ",count)
# output_Sudoku(output)