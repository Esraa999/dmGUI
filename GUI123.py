import tkinter as tk


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=555,
            width=312,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        canvas.create_rectangle(
            0.0,
            0.0,
            312.1875,
            555.0,
            fill="#D9D9D9",
            outline=""
        ) 
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1):
  
            frame = F(container, self, canvas)

            # initializing frame of that object from
            # startpage, page1 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
        # check if the current frame is StartPage
        if cont == StartPage:
            # switch to Page1 after 2 seconds
            self.after(2000, lambda: self.show_frame(Page1))
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent,controller, canvas):
        tk.Frame.__init__(self, parent)  
        self.canvas = canvas       
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            155.0,
            102.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            0.0,
            308.0,
            314.0,
            555.1199951171875,
            fill="#FFFFFF",
            outline="")
        
        self.after(2000,Page1)

  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller,canvas):     
        tk.Frame.__init__(self, parent)
        button_image_1 = PhotoImage(
        file=relative_to_assets("arabic.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
        command = lambda : controller.show_frame(StartPage),
            relief="flat"
        )
        button_1.place(
            x=29.836456298828125,
            y=142.67752075195312,
            width=106.14338684082031,
            height=52.432281494140625
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("English.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
        command = lambda : controller.show_frame(StartPage),
            relief="flat"
        )
        button_2.place(
            x=174.98422241210938,
            y=142.67752075195312,
            width=106.14338684082031,
            height=52.432281494140625
        )

        canvas.create_text(
            26.0,
            96.0,
            anchor="nw",
            text="Choose Your Language Experience",
            fill="#85A222",
            font=("SansSerifCollection", 15 * -1)
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            157.0,
            25.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            0.0,
            308.0,
            314.0,
            555.1199951171875,
            fill="#FFFFFF",
            outline="")

        button_image_3 = PhotoImage(
            file=relative_to_assets("goback.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
        command = lambda : controller.show_frame(StartPage),
            relief="flat"
        )
        button_3.place(
            x=11.0,
            y=9.0,
            width=47.0,
            height=23.0
        )



# window = Tk()

# window.geometry("312x555")
# window.configure(bg = "#FFFFFF")

# Driver Code
app = tkinterApp()
app.mainloop()

# canvas = Canvas(
#     app,
#     bg = "#FFFFFF",
#     height = 555,
#     width = 312,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )

# canvas.place(x = 0, y = 0)
# canvas.create_rectangle(
#     0.0,
#     0.0,
#     312.1875,
#     555.0,
#     fill="#D9D9D9",
#     outline="")