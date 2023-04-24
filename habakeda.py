from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainPage:
    def __init__(self, master):
        self.master = master
        self.master.geometry("312x555")
        self.master.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.master,
            bg="#D9D9D9",
            height=555,
            width=312,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            312.1875,
            555.0,
            fill="#D9D9D9",
            outline=""
        )
        # self.image_1 = PhotoImage(
        #     file=relative_to_assets("image_1.png")
        #     )

        # self.canvas.create_image(
        #     155.0,
        #     102.0,
        #     image=self.image_1
        # )


        self.canvas.create_rectangle(
            0.0,
            308.0,
            314.0,
            555.1199951171875,
            fill="#FFFFFF",
            outline=""
        )

if __name__ == "__main__":
    root = Tk()
    app = MainPage(root)
    root.mainloop()