from texttable import Texttable

def createSudoku(path):
    f = open(f"{path}","r")
    mat=[]
    for line in f:
        row = [ int(i) for i in line.split(',') ]
        mat.append(row)
    return mat

def outputSudoku(mat):
    print("Output: ")
    t=Texttable()
    for i in mat:
        # print(*i)
        t.add_row(i)
    print(t.draw())

def input_Sudoku():
    mat=[]
    print("Input Sudoku: ")
    for _ in range(9):
        l=[int(i) for i in input().split()]
        mat.append(l)
    return mat