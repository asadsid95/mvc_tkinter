from tkinter import *
import controller

class View:
    def __init__(self):

        self.root = Tk()
    
        self.welcome = Label(self.root,text="Welcome to Movie Library").grid(row=0,column=0, columnspan=4)

        # input
        self.name_label = Label(self.root,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0, columnspan=1)
        self.name_entry = Entry(self.root,width=35)
        self.name_entry.grid(row=1,column=2, padx=10)

        self.date_label = Label(self.root,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0, columnspan=1)
        self.date_entry = Entry(self.root,width=35)
        self.date_entry.grid(row=2,column=2, padx=10)

        self.submit_title = Button(self.root, text="Submit Title", command=self.submit)
        self.submit_title.grid(row=3, column=0, columnspan=4, padx=10, pady=10,ipadx=100)

        self.controller = None

    # input based formatting (error? show red ; success? return msg)

    def set_controller(self,controller):
        self.controller = controller

    def submit(self):
        # get value from each Entry
        self.controller.save(self.name_entry.get())
        pass

    def execute(self):
        self.root.mainloop()


# View().execute()