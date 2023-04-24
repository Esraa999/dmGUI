from pathlib import Path
import tkinter as tk
from tkinter import *
import cv2
import threading
import time
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\admin\Downloads\Projects\GUI\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MainPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame1 = Frame(self.master, bg="#D9D9D9", width=312, height=555)
        self.frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.image_path = relative_to_assets("image_1.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.frame1, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.2, anchor=CENTER) # Position the label in the canvas

        # Get the global instance of the VideoPlayer class
        self.video_player = VideoPlayer.get_instance(self.frame1, "video.mp4")
        # Start the play method in a separate thread
        threading.Thread(target=self.video_player.play).start()
        self.video_player.place(relx=0.5,rely=0.8,anchor=CENTER)
                
        # self.video_player = VideoPlayer.get_instance(master, "video.mp4")
        # self.video_player.pack(side=BOTTOM, fill=X)
        # self.video_player.place(relx=0.5,rely=0.8,anchor=CENTER)
        # self.video_player.play()
        # self.frames = {}
        # for F in (MainPage, Page1):
        #     frame = F(self.master)
        #     self.frames[F] = frame
        #     frame.grid(row=0, column=0, sticky="nsew")
        
        self.master.after(2000, self.switch_to_another_frame)
    
    def switch_to_another_frame(self):
        self.image_label.destroy() # Remove the image label
        self.frame1.forget() # Forget the frame
        Page1(self.master) # Switch to Page1

class Page1(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        self.window = window
        self.frame = tk.Frame(window)
        
        self.create_widgets()
        
    def create_widgets(self):        
        self.frame1 = Frame(self.master, bg="#D9D9D9", width=312, height=555)
        self.frame1.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.video_player = VideoPlayer.get_instance(self.master, "video.mp4")
        self.image_path = relative_to_assets("image_1.png")
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = Label(self.frame1, image=self.photo)
        self.image_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.label1 = Label(self.frame1,bg="#D9D9D9", text="Choose Your Language Experience", font=("SansSerifCollection", 9))
        self.label1.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.button_image_1 = PhotoImage(file=relative_to_assets("arabic.png"))
        self.button_1 = Button(self.frame1,bg="#D9D9D9", image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("button_1 clicked"), relief="flat")
        self.button_1.place(relx=0.3, rely=0.4, anchor=CENTER)

        self.button_image_2 = PhotoImage(file=relative_to_assets("English.png"))
        self.button_2 = Button(self.frame1,bg="#D9D9D9", image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.switch_to_main_page, relief="flat")
        self.button_2.place(relx=0.7, rely=0.4, anchor=CENTER)

        self.button_image_3 = PhotoImage(file=relative_to_assets("goback.png"))
        self.button_3 = Button(self.frame1,bg="#D9D9D9", image=self.button_image_3, borderwidth=0, highlightthickness=0, command= self.switch_to_main_page, relief="flat")
        self.button_3.place(relx=0.05, rely=0.05)
    
    def switch_to_main_page(self):
        self.image_label.destroy()
        self.frame1.forget() # Forget the frame
        MainPage(self.master) # Switch to Page1
        

class VideoPlayer(tk.Frame):
    _instance = None
    
    def __init__(self, parent, video_path):
        if VideoPlayer._instance is not None:
            raise Exception("VideoPlayer is a singleton class. Use get_instance() method to get the instance.")
        
        tk.Frame.__init__(self, parent)
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.label = tk.Label(self.frame)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.play_thread = None
        self.is_playing = False
        
    @classmethod
    def get_instance(cls, parent, video_path):
        if cls._instance is None:
            cls._instance = cls(parent, video_path)
        return cls._instance
    
    def play(self):
        ret, frame = self.cap.read()
        if ret:
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            photo = ImageTk.PhotoImage(image)
            self.label.configure(image=photo)
            self.label.image = photo
        
        # Read the next frame after 33ms (30fps)
        self.after(3, self.play)
        
    def start_play_thread(self):
        self.is_playing = True
        self.play_thread = threading.Thread(target=self.play_loop)
        self.play_thread.start()
        
    def stop_play_thread(self):
        self.is_playing = False
        if self.play_thread is not None:
            self.play_thread.join()
            self.play_thread = None
        
    def play_loop(self):
        while self.is_playing:
            self.play()
            time.sleep(0.03) # Wait for 33ms (30fps)

if __name__ == "__main__":
    master = Tk()
    master.geometry("312x555")
    master.configure(bg="#D9D9D9")
    app = MainPage(master)
    master.mainloop()

    
# class VideoPlayer(tk.Frame):
#     _instance = None
    
#     def __init__(self, parent, video_path):
#         if VideoPlayer._instance is not None:
#             raise Exception("VideoPlayer is a singleton class. Use get_instance() method to get the instance.")
        
#         tk.Frame.__init__(self, parent)
#         self.video_path = video_path
#         self.cap = cv2.VideoCapture(video_path)
#         self.frame = tk.Frame(self)
#         self.frame.pack(fill=tk.BOTH, expand=True)
#         self.label = tk.Label(self.frame)
#         self.label.pack(fill=tk.BOTH, expand=True)
#         self.play_thread = None
#         self.is_playing = False
        
#     @classmethod
#     def get_instance(cls, parent, video_path):
#         if cls._instance is None:
#             cls._instance = cls(parent, video_path)
#         return cls._instance
        
#     def play(self):
#         ret, frame = self.cap.read()
#         if ret:
#             image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             image = Image.fromarray(image)
#             photo = ImageTk.PhotoImage(image)
#             self.label.configure(image=photo)
#             self.label.image = photo
        
#         # Read the next frame after 33ms (30fps)
#         self.after(33, self.play)
        
#     def start_play_thread(self):
#         self.is_playing = True
#         self.play_thread = threading.Thread(target=self.play_loop)
#         self.play_thread.start()
        
#     def stop_play_thread(self):
#         self.is_playing = False
#         if self.play_thread is not None:
#             self.play_thread.join()
#             self.play_thread = None
        
#     def play_loop(self):
#         while self.is_playing:
#             self.play()
#             time.sleep(0.03) # Wait for 33ms (30fps)
