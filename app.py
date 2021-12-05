import tkinter as tk
# import view 
import view2
from model import *
from controller import * 

class MainApp(tk.Tk): # subclass of toplevel widget
    def __init__(self):
        tk.Tk.__init__(self)
        # self.toplevel = toplevel
        self.title("This is from app.py") 
        
        print(view2.View(self).winfo_parent()) # This returns root window (i.e. '.' )

    pass

if __name__=="__main__":
    root = MainApp()
    # MainApp(root) # passing toplevel widget into MainApp object. This is required as class's constructor has an attribute (i.e. ). T
    root.mainloop()