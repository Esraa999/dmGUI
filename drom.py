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

class TimerThread(threading.Thread):
    def __init__(self, timeout, callback,window):
        threading.Thread.__init__(self)
        self.timeout = timeout
        self.callback = callback
        self.window = window
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
            self.event.wait(self.timeout)
            if not self.event.is_set():
                self.callback(self)

    def stop(self):
        self.event.set()
        self.join()

    def start_timer(self):
        self.timer_thread.start()  # start the timer thread

    def reset_timer(self):
        self.timer_thread.stop()  # stop the previous timer
        self.timer_thread = TimerThread(10, TimerThread.wait_page,self.window)# create a new timer thread
        self.timer_thread.start()  # start the new timer thread
    
    def wait_page(self):
        Waiting(self.window)

    def quit_app(self):
        MainPage(self.window)

class Waiting(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.frame = Frame(self.window) # create timer thread
        self.create_widgets()
        TimerThread.start_timer(self)

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
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)

        self.continue_img = PhotoImage(file=relative_to_assets("continue.png"))
        self.continue_but= Button(self.frame,bg="#D9D9D9", image=self.continue_img, borderwidth=0,command=lambda: self.GetNumber("3"), highlightthickness=0, relief="flat")
        self.continue_but.place(relx=0.167192,rely=0.2936936)
        
        self.quit_img = PhotoImage(file=relative_to_assets("quit.png"))
        self.quit_but= Button(self.frame,bg="#D9D9D9", image=self.quit_img, borderwidth=0,command= self.switch_to_Main, highlightthickness=0, relief="flat")
        self.quit_but.place(relx=0.54,rely=0.2936936)

    def switch_to_Main(self):
        TimerThread.reset_timer(self) # reset the timer
        self.image_label.destroy()
        self.frame.destroy() # Forget the frame
        MainPage(self.window) # Switch to Page1

class MainPage(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.frame = Frame(self.window, bg="#D9D9D9", width=312, height=555)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.2, anchor=CENTER) # Position the label in the canvas
        self.window.bind("<Button-1>", self.switch_to_another_frame)
        
    def switch_to_another_frame(self, event):
        self.image_label.destroy() # Remove the image label
        self.frame.destroy() # Forget the frame
        Page1.focus_set(self)
        Page1(self.window) # Switch to Page1

class Page1(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.frame = Frame(window)# create timer thread
        self.timer_thread = TimerThread(5, TimerThread.wait_page,self.window)  # create timer thread
        self.create_widgets()
        TimerThread.start_timer(self)
  
    def create_widgets(self):        
        self.frame = Frame(self.window, bg="#D9D9D9", width=312, height=555)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label1 = Label(self.frame,bg="#D9D9D9", text="Choose Your Language Experience", font=("SansSerifCollection", 9))
        self.label1.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.button_image_1 = PhotoImage(file=relative_to_assets("arabic.png"))
        self.button_1 = Button(self.frame,bg="#D9D9D9", image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(relx=0.3, rely=0.4, anchor=CENTER)

        self.button_image_2 = PhotoImage(file=relative_to_assets("English.png"))
        self.button_2 = Button(self.frame,bg="#D9D9D9", image=self.button_image_2, borderwidth=0, highlightthickness=0, command= self.switch_to_Page1, relief="flat")
        self.button_2.place(relx=0.7, rely=0.4, anchor=CENTER)

        self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
        self.back = Button(self.frame,bg="#D9D9D9", image=self.back_img, borderwidth=0, highlightthickness=0, command= self.switch_to_main_page, relief="flat")
        self.back.place(relx=0.05, rely=0.05)
        self.frame.pack()

    def switch_to_Page1(self):
        TimerThread.reset_timer(self)  # reset the timer
        self.image_label.destroy()
        self.frame.destroy() # Forget the frame
        Page2(self.window) # Switch to Page1

    def switch_to_main_page(self):
        TimerThread.reset_timer(self)  # reset the timer
        self.frame.destroy() # Forget the frame
        MainPage(self.window) # Switch to Page1

class Page2(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.frame = Frame(window)
        self.timer_thread = TimerThread(5, TimerThread.wait_page,self.window)  # create timer thread
        self.create_widgets()
        TimerThread.start_timer(self)
  
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
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)

        label_1 = Label(
        self.frame,
        text="Phone Number",
        bg="#D9D9D9",
        fg="#404921",
        font=("Inter", 11)
        )
        label_1.place(
            relx=0.5,
            rely=0.119,
            anchor=CENTER
        )
        
        self.file=relative_to_assets("entry_1.png")
        self.entry_image_1  = Image.open(self.file)
        self.img = ImageTk.PhotoImage(self.entry_image_1)

        self.entry_image_1_label= Label(self.frame, image=self.img,bg="#D9D9D9")
        self.entry_image_1_label.place(relx=0.5, rely=0.179, anchor=CENTER)

        self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
        self.back = Button(self.frame,bg="#D9D9D9", image=self.back_img, borderwidth=0, highlightthickness=0, command= self.switch_to_Page1, relief="flat")
        self.back.place(relx=0.05, rely=0.03)

        entry_1 = Entry(
            self.frame,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            relx=0.2207133757961783,
            rely=0.149,
            width=174.3867359161377,
            height=28.448471069335938
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2= Button(self.frame,bg="#D9D9D9", image=self.button_image_2,command=lambda: self.GetNumber("1"), borderwidth=0, highlightthickness=0, relief="flat")
        self.button_2.place(relx=0.21,rely=0.214)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        self.button_3= Button(self.frame,bg="#D9D9D9", image=self.button_image_3, borderwidth=0, command=lambda: self.GetNumber("2"),highlightthickness=0, relief="flat")
        self.button_3.place(relx=0.41,rely=0.214)

        self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.button_4= Button(self.frame,bg="#D9D9D9", image=self.button_image_4, borderwidth=0,command=lambda: self.GetNumber("3"), highlightthickness=0, relief="flat")
        self.button_4.place(relx=0.61,rely=0.214)

        self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.button_5= Button(self.frame,bg="#D9D9D9",image=self.button_image_5, borderwidth=0, highlightthickness=0, relief="flat", command=lambda: self.GetNumber("4"))
        self.button_5.place(relx=0.21,rely=0.283)

        self.button_image_6= PhotoImage(file=relative_to_assets("button_6.png"))
        self.button_6= Button(self.frame,bg="#D9D9D9", image=self.button_image_6, borderwidth=0,command=lambda: self.GetNumber("5"), highlightthickness=0, relief="flat")
        self.button_6.place(relx=0.41,rely=0.283)

        self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
        self.button_7= Button(self.frame,bg="#D9D9D9", image=self.button_image_7, borderwidth=0, highlightthickness=0, command=lambda: self.GetNumber("6"),relief="flat")
        self.button_7.place(relx=0.61,rely=0.283)
        
        self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
        self.button_8 = Button(self.frame,bg="#D9D9D9", image=self.button_image_8, borderwidth=0,command=lambda: self.GetNumber("9"), highlightthickness=0, relief="flat")
        self.button_8.place(relx=0.61,rely=0.351)
        
        self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
        self.button_9= Button(self.frame,bg="#D9D9D9", image=self.button_image_9, borderwidth=0,command=lambda: self.GetNumber("8"), highlightthickness=0, relief="flat")
        self.button_9.place(relx=0.41,rely=0.351)

        self.button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
        self.button_10= Button(self.frame,bg="#D9D9D9", image=self.button_image_10, borderwidth=0,command=lambda: self.GetNumber("7"), highlightthickness=0, relief="flat")
        self.button_10.place(relx=0.21,rely=0.351)

        self.button_image_0 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_10= Button(self.frame,bg="#D9D9D9", image=self.button_image_0, borderwidth=0,command=lambda: self.GetNumber("0"), highlightthickness=0, relief="flat")
        self.button_10.place(relx=0.41,rely=0.419)


        self.verify_p = PhotoImage(file=relative_to_assets("verify.png"))
        self.verify= Button(self.frame,bg="#D9D9D9", image=self.verify_p,command=self.switch_to_Page3,borderwidth=0, highlightthickness=0, relief="flat")
        self.verify.place(relx=0.5,rely=0.518,anchor=CENTER)
        self.frame.pack()

    def switch_to_Page3(self):
        TimerThread.reset_timer(self)  # reset the timer
        self.frame.destroy() # Forget the frame
        score = 9
        Page3(self.window,score)
    
    def switch_to_Page1(self):
        TimerThread.reset_timer(self)  # reset the timer
        self.frame.destroy() # Forget the frame
        Page1(self.window)
    
    my_string = ""

    def GetNumber(self,letter):
        TimerThread.reset_timer(self)  # reset the timer
        self.my_string
        self.my_string += letter
        print(self.my_string)

class Page3(Frame):
    def __init__(self, window,score):
        Frame.__init__(self, window)
        self.window = window
        self.timer_thread = TimerThread(5, TimerThread.wait_page,self.window)  # create timer thread
        self.create_widgets(score)
        TimerThread.start_timer(self)

    def create_widgets(self,score):      
        self.frame = Frame(
            self.window,
            bg="#D9D9D9",
            height=555,
            width=314,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.score=str(score)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.image_path = relative_to_assets("logo.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)
        
        self.p= relative_to_assets("arrow.png")
        self.arrow= Image.open(self.p)
        self.arrowP= ImageTk.PhotoImage(self.arrow)
        self.arrowP_label = Label(self.frame, bg="#D9D9D9",image=self.arrowP)
        self.arrowP_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        self.image_label = Label(self.frame, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER)
        label_1 = Label(
        self.frame,
        text="Credit "+self.score,
        bg="#D9D9D9",
        fg="#8FAF20",
        font=("Inter", 11)
        )

        label_1.place(
            relx=0.5,
            rely=0.15,
            anchor=CENTER
        )
        
        self.file=relative_to_assets("basket.png")
        self.basket  = Image.open(self.file)
        self.baskett= ImageTk.PhotoImage(self.basket)

        self.basket_label= Label(self.frame, image=self.baskett,bg="#D9D9D9")
        self.basket_label.place(relx=0.73, rely=0.2)

        self.file=relative_to_assets("Bottle.png")
        self.bottle= Image.open(self.file)
        self.bottle_img= ImageTk.PhotoImage(self.bottle)

        self.bottle_label= Label(self.frame, image=self.bottle_img,bg="#D9D9D9")
        self.bottle_label.place(relx=0.13, rely=0.2)
                
        self.recycle = PhotoImage(
            file=relative_to_assets("Recycle.png"))
        self.recycle_button = Button(
            self.frame,
            image=self.recycle,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=lambda: print("recycle clicked"),
            relief="flat"
        )
        self.recycle_button.place(
            relx=0.14562,
            rely=0.35
        )
        
        self.finsh = PhotoImage(
            file=relative_to_assets("finish.png"))
        self.finish_button = Button(
            self.frame,image=self.finsh,
            borderwidth=0,
            bg="#D9D9D9",
            highlightthickness=0,
            command=self.switch_to_Page4,
            relief="flat"
        )
        self.finish_button.place(
            relx=0.56,
            rely=0.35
        )
        
    def switch_to_Page4(self):
        TimerThread.reset_timer(self)
        self.frame.destroy() # Forget the frame
        Page4(self.window) # Switch to Page1

class Page4(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.timer_thread = TimerThread(5, TimerThread.wait_page,self.window)  # create timer thread
        self.create_widgets()
        TimerThread.start_timer(self)
  

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
    
    def switch_to_Page5(self):
        TimerThread.reset_timer(self)  # reset the timer
        self.frame.destroy() # Forget the frame
        Page5(self.window)

class Page5(Frame):
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
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_1 = Label(
        self.frame,
        text="THANK YOU \nFOR RECYCLING",
        bg="#D9D9D9",
        fg="#404921",
        font=("Inter", 11)
        )
        label_1.place(
            relx=0.5,
            rely=0.25,
            anchor=CENTER
        )
        self.window.after(7000, MainPage(self.window))

# class VideoPlayer:
#     def __init__(self, video_path):
#         self.video_path = video_path
#         self.initialize_opencv()
        
#     def initialize_opencv(self):
#         self.cap = cv2.VideoCapture(self.video_path)
#         cv2.namedWindow('Video Player', cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_EXPANDED)

#     def run_loop(self):
#         while True:
#             ret, frame = self.cap.read()
#             if ret:
#                 cv2.imshow('Video Player', frame)
#             else:
#                 self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 self.cap.release()
#                 cv2.destroyAllWindows()
#                 break
# def motion(event):
    # x, y = event.x, event.y
    # print('{}, {}'.format(x, y))


def tkinter_loop():
    window = tk.Tk()
    window.geometry("312x555")
    window.configure(bg="#D9D9D9")
    app = MainPage(window)
    # window.bind('<Motion>', motion)
    
    window.mainloop()

# def pygame_loop():
#     path = "C:/Users/admin/Downloads/Projects/GUI/build/video.mp4"
#     player = VideoPlayer(path)
#     player.run_loop()

if __name__ == "__main__":
    # pygame_thread = threading.Thread(target=pygame_loop)
    # pygame_thread.start()
    tkinter_loop()