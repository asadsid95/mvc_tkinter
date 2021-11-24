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

    # validation -> setting new values to self.email 'read-only' attribute via setter
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

class View(Frame):
    def __init__(self,parent):
        super().__init__(parent)

        self.label = Label(self, text="Email:")
        self.label.grid(row=1,column=0)

        self.email_var = StringVar()
        self.email_entry = Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1)

        self.save_button = Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3)

        self.message_label = Label(self, text='')
        self.message_label.grid(row=2,column=1)

        self.controller = None

    # sets the controller
    def set_controller(self, controller):
        self.controller = controller

    # controller will handle the saving of text upon button click
    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self,message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')    

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def save(self, email):
        try:
            self.model.email = email
            self.model.save()

            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            self.view.show_error(error)

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('MVC practise')

        model = Model("hello@hello.com")
        
        view = View(self)
        view.grid(row=0,column=0)

        controller = Controller(model, view)

        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()
