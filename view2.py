import tkinter as tk
from tkinter.constants import VERTICAL

class View(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.canvas_on_View_frame = tk.Canvas(self.parent)#.grid(row=0,column=0)
        self.frame_in_canvas = tk.Frame(self.canvas_on_View_frame)#.grid(row=0,column=0) 
        self.scroll = tk.Scrollbar(self.parent, orient=VERTICAL, command=self.canvas_on_View_frame.yview)

        self.canvas_on_View_frame.config(yscrollcommand= self.scroll.set)
        self.scroll.pack(side="right", fill="y") # .grid(row=0,column=2)
        self.canvas_on_View_frame.create_window((2,2), window=self.frame_in_canvas, anchor='nw')

        # self.welcome = tk.Label(self.frame_in_canvas,text="Welcome to Movie Library").grid(row=0,column=0)

        # self.name_label = tk.Label(self.frame_in_canvas,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0)
        # self.name_entry = tk.Entry(self.frame_in_canvas,width=35)
        # self.name_entry.grid(row=1,column=1, padx=10)

        # self.date_label = tk.Label(self.frame_in_canvas,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0)
        # self.date_entry = tk.Entry(self.frame_in_canvas,width=35)
        # self.date_entry.grid(row=2,column=1, padx=10)

        # self.submit_button = tk.Button(self.frame_in_canvas, text="Submit", command=self.submit)
        # self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10,ipadx=50)        

        # self.reset_button = tk.Button(self.frame_in_canvas, text="Reset View", command=self.reset)
        # self.reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10,ipadx=50)        

    def submit(self):
        print('Submitted!')

    def reset(self):
        print('Resetted!')

    def set_controller(self,controller):
        print('hello')
    pass