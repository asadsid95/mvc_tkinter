import tkinter as tk
from tkinter.constants import BOTH, COMMAND, LEFT, NS, RIGHT, VERTICAL, Y

class View(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # print(self.winfo_parent()) # This returns root window (i.e. '.' )
        # print(self.parent.winfo_parent()) # This also returns root window (i.e. blank )

        # Now that I know its been root window that has been created, now I'll first create a Frame
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=BOTH, expand=1)
        # print(self.main_frame.winfo_parent())

        # Create a Canvas in main_frame
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # print(self.my_canvas.winfo_parent()) # This returns .!view.!frame

        # Lets create scrollbar on my_canvas
        self.my_scrollbar = tk.Scrollbar(self.my_canvas,orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        self.my_canvas.config(yscrollcommand=self.my_scrollbar)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox('all')))

        # Creating another Frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas)

        # self.canvas_on_View_frame = tk.Canvas(self) # I assume self is referring to View Object which inherits Frame
        # self.frame_in_canvas = tk.Frame(self.canvas_on_View_frame)#.grid(row=0,column=0) 
        # self.scroll = tk.Scrollbar(self.canvas_on_View_frame, orient=VERTICAL, command=self.canvas_on_View_frame.yview)

        # self.welcome = tk.Label(self.frame_in_canvas,text="Welcome to Movie Library").grid(row=0,column=0)

        # self.canvas_on_View_frame.config(yscrollcommand= self.scroll.set)
        # self.canvas_on_View_frame.grid(row=0,column=0)
        # self.scroll.grid(row=0,column=1, sticky=NS) # .grid(row=0,column=2)
        # self.canvas_on_View_frame.create_window(2,2, window=self.frame_in_canvas, anchor='nw')

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