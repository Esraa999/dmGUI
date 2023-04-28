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
        self.frame = Frame(window) # create timer thread
        self.create_widgets()
  
    def create_widgets(self):       
        self.frame1 = Frame(
            self.window,
            bg="#D9D9D9",
            height=555,
            width=314,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.frame1, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)

        self.continue_img = PhotoImage(file=relative_to_assets("continue.png"))
        self.continue_but= Button(self.frame1,bg="#D9D9D9", image=self.continue_img, borderwidth=0,command=lambda: self.GetNumber("3"), highlightthickness=0, relief="flat")
        self.continue_but.place(relx=0.167192,rely=0.2936936)
        
        self.quit_img = PhotoImage(file=relative_to_assets("quit.png"))
        self.quit_but= Button(self.frame1,bg="#D9D9D9", image=self.quit_img, borderwidth=0,highlightthickness=0, relief="flat")
        self.quit_but.place(relx=0.54,rely=0.2936936)

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