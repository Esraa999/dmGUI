from pathlib import Path
import tkinter as tk
from tkinter import *
import cv2
import threading
import time
from PIL import Image, ImageTk
from pygame import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class Page2(Frame):   
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.create_widgets()

    def create_widgets(self):      
        self.frame = Frame(
            self.window,
            bg="#D9D9D9",
            height=555,
            width=314,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
        self.back = Button(self.frame,bg="#D9D9D9", image=self.back_img, borderwidth=0, highlightthickness=0, relief="flat")
        self.back.place(relx=0.05, rely=0.05)
        
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)
        Label(
            text="Receipt",
            fg="#8FAF20",
            bg="#D9D9D9",
            font=("Arial BoldMT", 16),
        ).place(x=122.44403076171875, y=62)

        Label(
            text="ITEMS",
            fg="#A6A3A3",bg="#D9D9D9",
            font=("Arial BoldMT", 7),
        ).place(x=28.6470947265625, y=92)

        Label(
            text="QTY",
            fg="#A6A3A3",bg="#D9D9D9",
            font=("Arial BoldMT", 7),
        ).place(x=145.15277099609375, y=92)

        Label(
            text="PRICE",
            fg="#A6A3A3",bg="#D9D9D9",
            font=("Arial BoldMT", 7),
        ).place(x=256.7218017578125, y=92)
        self.print_img = PhotoImage(file=relative_to_assets("print.png"))
        self.print_but= Button(self.frame,bg="#D9D9D9", image=self.print_img,command=self.switch_to_Page5, borderwidth=0, highlightthickness=0, relief="flat")
        self.print_but.place(x=110.59600830078125,y=211.510009765625,)
    
    def switch_to_Page5(self):  # reset the timer
        self.frame.destroy() # Forget the frame

def tkinter_loop():
    master = tk.Tk()
    master.geometry("312x555")
    master.configure(bg="#D9D9D9")
    app = Page2(master)
    # master.bind('<Motion>', motion)
    
    master.mainloop()

if __name__ == "__main__":
    # pygame_thread = threading.Thread(target=pygame_loop)
    # pygame_thread.start()
    tkinter_loop()