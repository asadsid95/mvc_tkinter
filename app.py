import tkinter as tk
# import view 
import view2
from model import *
from controller import * 

class MainApp(tk.Frame):
    def __init__(self,parent): # parent refers to root being passed as attribute to MainApp (@ the bottom)
        # super().__init__()
        tk.Frame.__init__(self,parent) # here we call 
        self.parent=parent
        self.parent.title('This is after Tk() passed as attribute to App()')
        self.parent['bg'] = 'blue'
        
        test_label = tk.Label(self, text = 'test').grid(row=0,column=0)

        # self.columnconfigure(0,weight=1)
        # self.rowconfigure(0,weight=1)
        
        # ui_model = Model('','')
        # ui_view = view.View(self)
        # ui_view = view2.View(self)
        # ui_view.grid(row=0,column=0)
        # controller = Controller(ui_model, ui_view)
        
        # ui_view.set_controller(controller)

if __name__=="__main__":
    root = tk.Tk()
    MainApp(root).pack(side='top', fill='y')
    root.mainloop()