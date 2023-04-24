import tkinter as tk

class Page1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text="This is Page 1")
        self.label.pack()
        self.button = tk.Button(self, text="Go to Page 2", command=self.goto_page2)
        self.button.pack()
    
    def goto_page2(self):
        self.pack_forget()  # remove all widgets from Page 1
        self.master.switch_frame(Page2)  # display widgets of Page 2

class Page2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.label = tk.Label(self, text="This is Page 2")
        self.label.pack()
        self.button = tk.Button(self, text="Go to Page 1", command=self.goto_page1)
        self.button.pack()
    
    def goto_page1(self):
        self.pack_forget()  # remove all widgets from Page 2
        self.master.switch_frame(Page1)  # display widgets of Page 1

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.switch_frame(Page1)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self.master)
        new_frame.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.pack()
    root.mainloop()
