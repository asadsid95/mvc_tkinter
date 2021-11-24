from tkinter import *

class View:
    def __init__(self) -> None:
        self.root = Tk()

        self.title_label = Label(self.root, text="Title")
        self.title_label.grid(row=0,column=0)

        self.title_entry = Entry(self.root, width=30)
        self.title_entry.grid(row=0, column=1)

        self.submit = Button(self.root, text="Submit", command=self.submit)
        self.submit.grid(row=1, column =0,columnspan=2)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def submit(self):
        # call controller, send user input to controller by using controller's specific method
        self.controller.passing(self.title_entry.get())

    def execute(self):
        self.root.mainloop()

class Controller:
    def __init__(self,model, view) -> None:
        self.model = model
        self.view = view

    def passing(self,title):
        self.model.title = title

class Model:
    def __init__(self, title) -> None:
        self.title = title

    def work(self):
        print(self.title)

class App():
    ui_model = Model("")
    ui_view = View()
    ui_controller = Controller(ui_model, ui_view)

    ui_view.set_controller(ui_controller)

    ui_view.execute()
