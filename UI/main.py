from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty


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
    def loadmat(self):
        self.mat= sudoku
        for i in range(9):
            for j in range(9):
                button = self.ids[f'{9*i+j}']
                if self.mat[i][j]!=0:
                    button.text = f'{self.mat[i][j]}'
                    self.lockedcells.append(button)
                else:
                    button.text = ' '
        
    def btn(self,id):
        # print(id,id.text)
        temp = get_key(self.ids,id)
        # print(f'temp val {temp}')
        self.currentButtonid=str(temp)
        # for key, val in self.ids.items():
        #     print("key={0}, val={1}".format(key, val))
    
    def choicebtn(self,id):
        button = self.ids[self.currentButtonid]
        temp = get_key(self.ids,id)
        print(id)
        print(button.text)
        print(self.ids[temp].text)
        if button not in self.lockedcells:
            button.text= self.ids[temp].text


class Mainapp(App):
    def build(self):
        return HomeScreen()


if __name__ == "__main__":
    app = Mainapp()
    app.run()
