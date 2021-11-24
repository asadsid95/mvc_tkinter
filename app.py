from tkinter import *
import view 
from model import *
from controller import * 

class App(Tk):
    def __init__(self):
        super().__init__()
    
        ui_model = Model('Dark')
        ui_view = view.View(self)
        ui_view.grid(row=0,column=0)

        controller = Controller(ui_model, ui_view)
        ui_view.set_controller(controller)


if __name__=="__main__":
    app = App()
    app.mainloop()