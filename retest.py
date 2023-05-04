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
        self.quit_but= Button(self.frame1,bg="#D9D9D9", image=self.quit_img, command = Popup, borderwidth=0,highlightthickness=0, relief="flat")
        self.quit_but.place(relx=0.54,rely=0.2936936)
    
    def switch_to_Page4(self):
        self.frame.destroy() # Forget the frame
        Popup(self.window) # Switch to Page1

class Popup(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        self.entry = tk.Entry(self)
        self.entry.pack(side="top", fill="x", padx=20, pady=10)

        self.continue_img = PhotoImage(file=relative_to_assets("continue.png"))
        self.continue_but= Button(self,bg="#D9D9D9", image=self.continue_img, borderwidth=0,command=lambda: self.GetNumber("3"), highlightthickness=0, relief="flat")
        self.continue_but.place(relx=0.167192,rely=0.2936936)
        
        self.quit_img = PhotoImage(file=relative_to_assets("quit.png"))
        self.quit_but= Button(self,bg="#D9D9D9", image=self.quit_img, borderwidth=0,command= self.cancel, highlightthickness=0, relief="flat")
        self.quit_but.place(relx=0.54,rely=0.2936936)

        self.result = None

    def ok(self):
        self.result = self.entry.get()
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()

# def create_popup():
#     # create a Toplevel window
#     def __init__(self):
#         popup = tk.Toplevel()
        
#         # # add widgets to the Toplevel window
#         # label = tk.Label(popup, text="This is a popup window!")
#         # label.pack(padx=20, pady=20)
        
#         # button = tk.Button(popup, text="Close", command=popup.destroy)
#         # button.pack(pady=10)
#         self.create_widgets()
#         # TimerThread.start_timer(self)

#     def create_widgets(self):
#         self.frame = Frame(
#             self.window,
#             bg="#D9D9D9",
#             height=555,
#             width=314,
#             bd=0,
#             highlightthickness=0,
#             relief="ridge"
#         )
#         self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
#         self.image_path = relative_to_assets("logo.png")
#         self.image = Image.open(self.image_path)
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.image_label = Label(self.frame, image=self.photo)
#         self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)

#         self.continue_img = PhotoImage(file=relative_to_assets("continue.png"))
#         self.continue_but= Button(self.frame,bg="#D9D9D9", image=self.continue_img, borderwidth=0,command=lambda: self.GetNumber("3"), highlightthickness=0, relief="flat")
#         self.continue_but.place(relx=0.167192,rely=0.2936936)
        
#         self.quit_img = PhotoImage(file=relative_to_assets("quit.png"))
#         self.quit_but= Button(self.frame,bg="#D9D9D9", image=self.quit_img, borderwidth=0,command= self.switch_to_Main, highlightthickness=0, relief="flat")
#         self.quit_but.place(relx=0.54,rely=0.2936936)

#     def switch_to_Main(self):
#         # TimerThread.reset_timer(self) # reset the timer
#         self.image_label.destroy()
#         self.frame.destroy() # Forget the frame
#         Page2(self.window) # Switch to Page1

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