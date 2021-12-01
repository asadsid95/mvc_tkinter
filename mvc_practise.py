# Practising creating movie library with MVC pattern b/c I don't understand how data flow is happening
from tkinter import *





# If we want to do something with the input data from View, we have to pass it to model via controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def passToModel(self):
        print(self.model)
    pass

class View:
    def __init__(self):
        self.root = Tk()
        self.name_label = Label(self.root, text="Enter title",padx=10,pady=10).grid(row=0,column=0)
        self.date_label = Label(self.root, text="Enter date",padx=10,pady=10).grid(row=1,column=0)
        self.name_entry = Entry(self.root,width=10)
        self.name_entry.grid(row=0, column=1)
        self.date_entry = Entry(self.root,width=10)
        self.date_entry.grid(row=1, column=1)

        self.submit_button = Button(self.root,text="Submit",command=self.submit,width=20).grid(row=3,column=0,columnspan=2)

        mainloop()

    def submit(self):
        print(self.name_entry.get())
        new_cont = Controller(self.name_entry.get(), self.date_entry.get()).passToModel()
        print(new_cont)
    pass
View()
class Model:
    pass

class App:

    pass