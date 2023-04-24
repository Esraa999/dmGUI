from pathlib import Path

from tkinter import *
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Page1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)   
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 555,
            width = 312,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            312.1875,
            555.0,
            fill="#D9D9D9",
            outline="")

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
        self.button = tk.Button(self, text="Go to Page 2", command=self.goto_page2)
        self.button.pack()
        
    def goto_page2(self):
        self.pack_forget()  # remove all widgets from Page 1
        self.master.switch_frame(Page2)  # display widgets of Page 2

class Page2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)   
        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 555,
            width = 312,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            312.1875,
            555.0,
            fill="#D9D9D9",
            outline="")
        
        canvas.create_rectangle(
            0.0,
            308.0,
            314.0,
            555.1199951171875,
            fill="#FFFFFF",
            outline="")
        self.button = tk.Button(self, text="Go to Page 2", command=self.goto_page2)
        self.button.pack()
        
    def goto_page2(self):
        self.pack_forget()  # remove all widgets from Page 1
        self.master.switch_frame(Page1)  # display widgets of Page 2

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("My App")
        window.geometry("312x555")
        window.configure(bg = "#FFFFFF")
        self.switch_to_page1(Page1)
    
    def switch_to_page1(self, frame_class):
        new_frame = frame_class(self.master)
        new_frame.pack()
        self.after(2000, self.switch_to_page2)

    def switch_to_page1(self, frame_class):
        new_frame = frame_class(self.master)
        new_frame.pack()

if __name__ == "__main__":
    window= tk.Tk()    
    app = MainApplication(window)
    app.pack()
    window.mainloop()