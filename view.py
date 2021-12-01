from tkinter import *
from PIL import ImageTk, Image
from urllib import request

class View(Frame):
    def __init__(self, parent):
        super().__init__(parent) 

        self.welcome = Label(self,text="Welcome to Movie Library").grid(row=0,column=0, columnspan=2)

        # input
        self.name_label = Label(self,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0, columnspan=1)
        self.name_entry = Entry(self,width=35)
        self.name_entry.grid(row=1,column=1, padx=10)

        self.date_label = Label(self,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0, columnspan=1)
        self.date_entry = Entry(self,width=35)
        self.date_entry.grid(row=2,column=1, padx=10)

        self.submit_title = Button(self, text="Submit Title", command=self.submit)
        self.submit_title.grid(row=3, column=0, columnspan=2, padx=10, pady=10,ipadx=50)

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
            self.date_entry.delete(0,END)
        elif self.date_entry.get() == '':
            self.controller.save(self.name_entry.get(), None)
            self.name_entry.delete(0,END)


    # functionality for incoming data from DB
    def receiving(self,movies):
        self.result=''

        self.image=[]
        canvas = Canvas(self, width=250, height=550, bg='white')
        canvas.grid(row=4, column=1)

        for movie in movies:
            self.result += str(movie[0]) + "\t" + str(movie[1]) + "\t" + str(movie[2]) +  "\t" + str(movie[3]) + "\n"
            self.image.append(ImageTk.PhotoImage(Image.open(request.urlopen(movie[4])).resize((200,250))))
            
        self.movie_info = Label(self, text=self.result, width=50)
        self.movie_info.grid(row=4,column=0, columnspan=1)  

        # for image in self.image:
        canvas.create_image(150,150, image=self.image[0])
        canvas.create_image(150,250, image=self.image[1])

        
        # for image in self.image:
            # self.movie_poster.pack()
            # self.movie_poster.grid(row=4,column=1, columnspan=1, padx=10, pady=10)

