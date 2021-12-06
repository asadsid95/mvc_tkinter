import tkinter as tk
from tkinter.constants import BOTH, COMMAND, LEFT, NS, NW, RIGHT, TOP, VERTICAL, Y
from PIL import ImageTk, Image
from urllib import request

class View(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # print(self.winfo_parent()) # This returns root window (i.e. '.' )
        # print(self.parent.winfo_parent()) # This also returns root window (i.e. blank )

        # Now that I know its been root window that has been created, I'll first create a Frame
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack(fill=BOTH, expand=1)
        # print(self.main_frame.winfo_parent())

        # Then create a Canvas in main_frame
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # print(self.my_canvas.winfo_parent()) # This returns .!view.!frame

        # Now Lets create scrollbar on my_canvas
        self.my_scrollbar = tk.Scrollbar(self.my_canvas,orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configuring the canvas for scrollbar's function
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox('all')))

        # Creating first Frame inside the canvas. First frame inside the canvas but second frame in total
        self.second_frame = tk.Frame(self.my_canvas)

        # Adding first frame to a window in the canvas
        self.my_canvas.create_window((0,0), window=self.second_frame, anchor=NW)

        self.welcome = tk.Label(self.second_frame,text="Welcome to Movie Library").grid(row=0,column=0)
        
        self.name_label = tk.Label(self.second_frame,text="Enter Movie name", padx=10, pady=10).grid(row=1,column=0)
        self.name_entry = tk.Entry(self.second_frame,width=35)
        self.name_entry.grid(row=1,column=1, padx=10)

        self.date_label = tk.Label(self.second_frame,text="Enter Date (YYYYMMDD) ", padx=10, pady=10).grid(row=2,column=0)
        self.date_entry = tk.Entry(self.second_frame,width=35)
        self.date_entry.grid(row=2,column=1, padx=10)

        self.submit_button = tk.Button(self.second_frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10,ipadx=50)        

        self.reset_button = tk.Button(self.second_frame, text="Reset View", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10,ipadx=50)        

        # Creating second Frame inside the canvas
        self.third_frame = tk.Frame(self.my_canvas)

        # Adding second Frame to a window in canvas
        self.my_canvas.create_window((0,200), window=self.third_frame, anchor=NW)

        self.controller = None

        # self.canvas_on_View_frame.config(yscrollcommand= self.scroll.set)
        # self.canvas_on_View_frame.grid(row=0,column=0)
        # self.scroll.grid(row=0,column=1, sticky=NS) # .grid(row=0,column=2)
        # self.canvas_on_View_frame.create_window(2,2, window=self.frame_in_canvas, anchor='nw')

    def set_controller(self,controller):
        self.controller = controller

    def submit(self):
        # get value from each Entry
        if self.name_entry.get() == '':
            self.controller.save(None, self.date_entry.get())
            # self.date_entry.delete(0,END)
        elif self.date_entry.get() == '':
            self.controller.save(self.name_entry.get(), None)

    def reset(self):
        print('Resetted!')

    def receiving(self,movies):
        # creating a frame inside third_frame w/ movie info on left & a movie-poster-containing-canvas on the right 
        # remember that each frame will go ultimately on third_frame
        
        # what if I create a canvas inside of third_frame, that will contain all frames mentioned above
        self.results_canvas = tk.Canvas(self.third_frame,bg='green')
        self.results_canvas.pack(side=TOP, fill=BOTH, expand=1)

        i=0
        for movie in movies:
            # Frame for each movie's info and poster
            self.movie_frame = tk.Frame(self.results_canvas,border=5, borderwidth=5)

            # label to show movie info
            tk.Label(self.movie_frame,text = movie[0],bg='yellow').grid(row=i,column=0)

            # create Photoimage 
            self.poster = ImageTk.PhotoImage(Image.open(request.urlopen(movie[4])).resize((200,250)))
            
            # create Canvas to contain movie poster
            self.poster_canvas = tk.Canvas(self.movie_frame, width=200, height=250)
            self.poster_canvas.grid(row=i, column=1)
            self.poster_canvas.create_image((100, i), image=self.poster)
            self.results_canvas.create_window((0,i*25), window=self.movie_frame, anchor=NW)

            i += 1
        # for row in range(len(movies)):
        #     tk.Label(self.third_frame, text=movies[row][0]).grid(row=row, column=0)
        # pass