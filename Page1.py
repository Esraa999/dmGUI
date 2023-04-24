from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\tkk\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("314x555")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 555,
    width = 314,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    1.0,
    0.0,
    313.1875,
    555.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("arabic.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    command=lambda: print("button_2 clicked"),
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
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=11.0,
    y=9.0,
    width=47.0,
    height=23.0
)
window.resizable(False, False)
window.mainloop()
