from tkinter import *

class View(Frame):
    def __init__(self, parent):
        super().__init__(parent) 

        self.welcome = Label(self,text="Welcome to Movie Library").grid(row=0,column=0, columnspan=4)

        # input
        self.name_label = Label(self,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0, columnspan=1)
        self.name_entry = Entry(self,width=35)
        self.name_entry.grid(row=1,column=2, padx=10)

        self.date_label = Label(self,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0, columnspan=1)
        self.date_entry = Entry(self,width=35)
        self.date_entry.grid(row=2,column=2, padx=10)

        self.submit_title = Button(self, text="Submit Title", command=self.submit)
        self.submit_title.grid(row=3, column=0, columnspan=4, padx=10, pady=10,ipadx=100)

        self.controller = None
    
    # To add: required input based formatting (error? show red ; success? return msg)

    # assigning value to controller of Controller object
    def set_controller(self,controller):
        self.controller = controller

    # send user input to controller object
    def submit(self):
        # get value from each Entry
        if self.name_entry.get() == '':
            self.controller.save(None, self.date_entry.get())
        elif self.date_entry.get() == '':
            self.controller.save(self.name_entry.get(), None)


    # create functionality for incoming data from DB
    def receiving(self,movies):
        result=''
        for movie in movies:
            result += str(movie[0]) + "\t" + str(movie[1]) + "\t" + str(movie[2]) +  "\t" + str(movie[3]) + "\n"
 
        movie_info = Label(self, text=result)
        movie_info.grid(row=4,column=0, columnspan=3)  

        # pass