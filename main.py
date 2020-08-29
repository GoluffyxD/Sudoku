from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from copy import deepcopy
from Modules.sudoku import *

sudoku =[
[0,0,7,0,0,0,0,0,4],
[0,0,0,6,5,0,0,0,2],
[0,2,0,8,0,1,0,6,0],
[0,1,0,0,0,0,0,0,0],
[0,0,0,0,4,0,7,8,5],
[5,0,2,0,0,0,0,0,0],       
[1,0,0,0,0,0,0,0,0],
[0,9,4,0,0,0,0,0,0],
[0,0,0,9,2,0,0,0,6]
]


def get_key(a,v):
    for key,val in a.items():
        if val==v:
            return key

class HomeScreen(Screen):
    currentButtonid = None
    mat = None
    lockedcells=[]
    locked = False

    def loadmat(self):
        self.mat= deepcopy(sudoku)
        for i in range(9):
            for j in range(9):
                button = self.ids[f'{9*i+j}']
                if self.mat[i][j]!=0:
                    button.text = f'{self.mat[i][j]}'
                    self.lockedcells.append(button)
                else:
                    button.text = ' '
        
    def btn(self,id):
        if self.locked == False:
            if self.currentButtonid != None:
                button = self.ids[self.currentButtonid]
                button.background_color=(1,1,1,1)
            temp = get_key(self.ids,id)
            self.currentButtonid=str(temp)
            id.background_color= (0,0,1,0.5)
    
    def choicebtn(self,id):
        button = self.ids[self.currentButtonid]
        temp = get_key(self.ids,id)
        if button in self.lockedcells:
            return
        x,y = int(self.currentButtonid)//9,int(self.currentButtonid) % 9
        val = int(self.ids[temp].text)
        possible = chkPossible(self.mat,x,y,val)
        if possible == False:
            if self.locked == True and button.text == self.ids[temp].text:
                button.text = ' '
                self.locked = False
                button.background_color=(1,1,1,1)
            else:
                button.background_color=(1,0,0,1)
                button.text= self.ids[temp].text
                self.locked = True
        else:
            self.locked = False
            if button.text == self.ids[temp].text:
                button.text = ' '
                self.mat[x][y] = 0
            else:
                button.text= self.ids[temp].text
                self.mat[x][y] = int(button.text)
            button.background_color=(1,1,1,1)

    def hint(self):
        val = solve_single_choice(self.mat)
        if val == -1:
            pass
        else:
            (x,y,value)=val
            self.ids[f'{9*x+y}'].text = f'{value}'
            self.ids[f'{9*x+y}'].background_color= (0,1,1,1)

class Mainapp(MDApp):

    def __init__(self, **kwargs):
        self.title = "Sudoku"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)

    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    app = Mainapp()
    app.run()
