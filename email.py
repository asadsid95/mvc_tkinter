from tkinter import *
import sqlite3
import re

class Model:

    def __init__(self, email) -> None: 
        self.email = email
    
    # Making email attribute read-only
    @property
    def email(self):
        return self.__email

    # setting new values to self.email 'read-only' attribute upon validation
    @email.setter
    def email (self, value):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        if re.fullmatch(pattern, value):
            self.__email = value
        else: 
            raise ValueError(f'Invalid entry: {value}')
        
    # Opens and appends to text file
    def save(self):
        with open('emails.txt', 'a') as file:
            file.write(self.email + '\n')

class View:
    def __init__(self):
        self.root = Tk()
        self.label = Label(self.root, text="Email:")
        self.label.grid(row=1,column=0)

    def run(self):
        self.root.mainloop()

View().run()
