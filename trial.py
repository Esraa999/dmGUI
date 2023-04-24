from pathlib import Path
import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
class MainPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("312x555")
        self.master.configure(bg="#FFFFFF")

        self.frame1 = Frame(self.master, bg="#D9D9D9", width=312, height=555)
        self.frame1.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.image_path = relative_to_assets("image_1.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.frame1, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label1 = Label(self.frame1, text="Choose Your Language Experience", font=("SansSerifCollection", 15))
        self.label1.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.button_image_1 = PhotoImage(file=relative_to_assets("arabic.png"))
        self.button_1 = Button(self.frame1, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.button_image_2 = PhotoImage(file=relative_to_assets("English.png"))
        self.button_2 = Button(self.frame1, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("button_2 clicked"), relief="flat")
        self.button_2.place(relx=0.7, rely=0.5, anchor=CENTER)

        self.button_image_3 = PhotoImage(file=relative_to_assets("goback.png"))
        self.button_3 = Button(self.frame1, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("button_3 clicked"), relief="flat")
        self.button_3.place(relx=0.05, rely=0.05)

if __name__ == "__main__":
    root = Tk()
    app = MainPage(root)
    root.mainloop()