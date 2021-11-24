from tkinter import *
from view import *
from model import *
from controller import * 

class App(Tk):
    
    ui_model = Model('random movie')
    ui_view = View(self)

    
if __name__=="__main__":
    App.mainloop()