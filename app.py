import tkinter as tk
# import view 
import view2
from model import *
from controller import * 

class MainApp:
    def __init__(self, toplevel): # constructor; This creates object with 1 attribute called 'self.toplevel' therefore I need to pass a value for it when instantiating
        self.toplevel = toplevel
        self.toplevel.title("This is being called from inside MainApp object. We've received tk.Tk() Widget as attribute")
        pass
    pass

if __name__=="__main__":
    root = tk.Tk()
    MainApp(root) # passing toplevel widget into MainApp object. This is required as class's constructor has an attribute (i.e. ). T
    root.mainloop()