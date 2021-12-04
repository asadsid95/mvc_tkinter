import tkinter as tk
# import view 
import view2
from model import *
from controller import * 

class MainApp(tk.Frame):
    def __init__(self, toplevel): # constructor; This creates object with 1 attribute called 'self.toplevel' therefore I need to pass a value for it when instantiating
        # tk.Frame.__init__(self,toplevel)
        self.toplevel = toplevel
        self.toplevel.title("This is being called from inside MainApp object. We've received tk.Tk() Widget as attribute")
        
        tk.Label(self.toplevel,text="Inside of Frame that ").grid(row=0,column=0)

        # Instead of creating Frame upon instantiation, I'm going to explore subclassing MainApp with Frame 
        #  
        # self.frame = tk.Frame(self.toplevel,bg='light green',width=75,height=90).grid(row=0,column=0)
        # label_in_Frame = tk.Label(self.frame, text="This is inside Frame, which is inside toplevel widget").grid(row=0,column=0)

    pass

if __name__=="__main__":
    root = tk.Tk()
    MainApp(root) # passing toplevel widget into MainApp object. This is required as class's constructor has an attribute (i.e. ). T
    # print(MainApp.__mro__)
    root.mainloop()