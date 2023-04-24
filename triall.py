from tkinter import *
from tkinter import ttk

from pathlib import Path

root = Tk()
root.geometry("310x340")
root.resizable(False, False)
root.configure(background="#F4F4F4")



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Define function to handle button click events
def button_clicked(number):
    print(f"Button {number} clicked")

# Create phone frame
phone_frame = Frame(root, bg="#F4F4F4")
phone_frame.pack(side=TOP, pady=20)

phone_label = Label(phone_frame, text="Phone Number", bg="#F4F4F4", fg="#404921", font=("Inter", 11))
phone_label.pack(side=TOP, padx=10, pady=10, anchor=W)

entry_frame = Frame(phone_frame, bg="#F4F4F4")
entry_frame.pack(padx=20, pady=10)

entry_image = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_label = Label(entry_frame, image=entry_image, bd=0)
entry_label.pack(side=LEFT)

entry_box = Entry(entry_frame, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_box.pack(side=LEFT, padx=(5, 0))

# Create button frame
button_frame = Frame(root, bg="#F4F4F4")
button_frame.pack(side=TOP, pady=10)

# Define button images
button_images = []
for i in range(1, 10):
    button_image = PhotoImage(file=relative_to_assets(f"button_{i}.png"))
    button_images.append(button_image)

# Create buttons
button_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]

for i, row in enumerate(button_grid):
    for j, button_number in enumerate(row):
        if button_number is not None:
            button_image = button_images[button_number-1]
            button = Button(button_frame, image=button_image, borderwidth=0, highlightthickness=0, 
                            command=lambda number=button_number: button_clicked(number),
                            relief="flat", bg="#D9D9D9")
            button.grid(row=i, column=j, padx=2, pady=2)
        else:
            ttk.Separator(button_frame, orient=VERTICAL).grid(row=i, column=j, padx=2, pady=2)

root.mainloop()
