from tkinter import Frame, Button, Label, Entry

class View(Frame):
    def __init__(self, parent):
        super().__init__(parent)
    
        frame_p = Frame(parent, bg='light blue',width=500, height=500).grid(row=0,column=0)
        # frame_test = Frame(parent, bg='light green',width=500, height=500).grid(row=1,column=0)

        self.welcome = Label(frame_p,text="Welcome to Movie Library").grid(row=0,column=0, columnspan=2)

        # input
        self.name_label = Label(frame_p,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0, columnspan=1)
        self.name_entry = Entry(frame_p,width=35)
        self.name_entry.grid(row=1,column=1, padx=10)

        self.date_label = Label(frame_p,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0, columnspan=1)
        self.date_entry = Entry(frame_p,width=35)
        self.date_entry.grid(row=2,column=1, padx=10)

        self.submit_button = Button(frame_p, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10,ipadx=50)
        
        # self.reset_button = Button(frame_p, text="Reset View", command=self.reset)
        # self.reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10,ipadx=50)

    def submit(self):
        print('Submitted!')

    def set_controller(self,controller):
        print('hello')
    pass