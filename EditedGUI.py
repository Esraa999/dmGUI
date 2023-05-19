import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import *
import cv2
import threading
import time
from PIL import Image, ImageTk
from tkvideo import tkvideo
import pygame
from pygame import *
import requests
from io import BytesIO


LARGEFONT =("Verdana", 12)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Esraa\Desktop\dmGUI-master\dmGUI-master\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, Page1, Page2,Page3,Page4,Page5):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	

# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.image_path = relative_to_assets("logo.png")
		self.image = Image.open(self.image_path)
		self.photo = ImageTk.PhotoImage(self.image)
		self.image_label = Label(image=self.photo)
		self.image_label.place(relx=0.5, rely=0.05, anchor=CENTER) # Position the label in the canvas
		self.image_path2 = ("C:\\Users\\Esraa\\Desktop\\dmGUI-master1\\dmGUI-master\\assets\\frame0\\start.png")
		self.image2 = Image.open(self.image_path2)
		self.photo2 = ImageTk.PhotoImage(self.image2)
		self.image_label2 = ttk.Button(self, image=self.photo2, command=lambda: controller.show_frame(Page1))
		self.image_label2.place(relx=0.5, rely=0.6, anchor=CENTER)# Position the label in the canvas
		#self.bind("<Button-1>")

# second window frame page1
class Page1(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
		self.back = ttk.Button(self,image=self.back_img, command=lambda: controller.show_frame(StartPage))
		self.back.place(relx=0.05, rely=0.05)
		self.label1 = ttk.Label(self,text="Choose Your Language Experience", font=("SansSerifCollection", 9))
		self.label1.place(relx=0.5, rely=0.4, anchor=CENTER)
		self.button_image_1 = PhotoImage(file=relative_to_assets("arabic.png"))
		self.button_1 = ttk.Button(self,image=self.button_image_1,command=lambda: controller.show_frame(Page1))
		self.button_1.place(relx=0.2, rely=0.7, anchor=CENTER)
		self.button_image_22 = PhotoImage(file=relative_to_assets("English.png"))
		self.button_22 = ttk.Button(self,image=self.button_image_22, command=lambda: controller.show_frame(Page2))
		self.button_22.place(relx=0.8, rely=0.7, anchor=CENTER)
		

		
		
# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
		self.back = ttk.Button(self,image=self.back_img, command=lambda: controller.show_frame(Page1))
		self.back.place(relx=0.05, rely=0.05)
		self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
		self.button_2= ttk.Button(self, image=self.button_image_2,command=lambda: self.GetNumber("1"))
		self.button_2.place(relx=0.17,rely=0.3)
		self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
		self.button_3= ttk.Button(self, image=self.button_image_3, command=lambda: self.GetNumber("2"))
		self.button_3.place(relx=0.41,rely=0.3)
		self.button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
		self.button_4= ttk.Button(self,image=self.button_image_4, command=lambda: self.GetNumber("3"))
		self.button_4.place(relx=0.65,rely=0.3)
		self.button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
		self.button_5= ttk.Button(self,image=self.button_image_5,command=lambda: self.GetNumber("4"))
		self.button_5.place(relx=0.17,rely=0.45)
		self.button_image_6= PhotoImage(file=relative_to_assets("button_6.png"))
		self.button_6= ttk.Button(self,image=self.button_image_6,command=lambda: self.GetNumber("5"))
		self.button_6.place(relx=0.41,rely=0.45)
		self.button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
		self.button_7= ttk.Button(self,image=self.button_image_7,command=lambda: self.GetNumber("6"))
		self.button_7.place(relx=0.65,rely=0.45)
		self.button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
		self.button_8 = ttk.Button(self, image=self.button_image_8,command=lambda: self.GetNumber("9"))
		self.button_8.place(relx=0.65,rely=0.6)
		self.button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
		self.button_9= ttk.Button(self, image=self.button_image_9, command=lambda: self.GetNumber("8"))
		self.button_9.place(relx=0.41,rely=0.6)
		self.button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
		self.button_10= ttk.Button(self, image=self.button_image_10,command=lambda: self.GetNumber("7"))
		self.button_10.place(relx=0.17,rely=0.6)
		self.button_image_0 = PhotoImage(file=relative_to_assets("button_1.png"))
		self.button_10= ttk.Button(self, image=self.button_image_0,command=lambda: self.GetNumber("0"))
		self.button_10.place(relx=0.41,rely=0.75)
		self.verify_p = PhotoImage(file=relative_to_assets("verify.png"))
		self.verify= ttk.Button(self, image=self.verify_p,command=lambda: controller.show_frame(Page3))
		self.verify.place(relx=0.82,rely=0.95,anchor=CENTER)
		
	my_string = ""
	def GetNumber(self,letter):
			self.my_string
			self.my_string += letter
			print(self.my_string)
        
class Page3(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
		self.back = ttk.Button(self,image=self.back_img, command=lambda: controller.show_frame(Page2))
		self.back.place(relx=0.05, rely=0.05)

		self.p= relative_to_assets("arrow.png")
		self.arrow= Image.open(self.p)
		self.arrowP= ImageTk.PhotoImage(self.arrow)
		self.arrowP_label = ttk.Label(self, image=self.arrowP)
		self.arrowP_label.place(relx=0.5, rely=0.5, anchor=CENTER)

		label_1 = ttk.Label(self,text="Credit ")
		label_1.place(relx=0.5,rely=0.35,anchor=CENTER)
		self.file=relative_to_assets("basket.png")
		self.basket  = Image.open(self.file)
		self.baskett= ImageTk.PhotoImage(self.basket)
		self.basket_label= ttk.Label(self, image=self.baskett)
		self.basket_label.place(relx=0.73, rely=0.4)
		self.file=relative_to_assets("Bottle.png")
		self.bottle= Image.open(self.file)
		self.bottle_img= ImageTk.PhotoImage(self.bottle)
		self.bottle_label= ttk.Label(self, image=self.bottle_img)
		self.bottle_label.place(relx=0.13, rely=0.4)
		self.recycle = PhotoImage(file=relative_to_assets("Recycle.png"))
		self.recycle_button = ttk.Button(self,image=self.recycle,command=lambda: print("recycle clicked"))
		self.recycle_button.place(relx=0.14562,rely=0.75)
		self.finsh = PhotoImage( file=relative_to_assets("finish.png"))
		self.finish_button = ttk.Button(self,image=self.finsh,command = lambda : controller.show_frame(Page4))
		self.finish_button.place(relx=0.56,rely=0.75)
		
class Page4(tk.Frame):
	def __init__(self, parent,controller):
		tk.Frame.__init__(self, parent)

		self.back_img = PhotoImage(file=relative_to_assets("goback.png"))
		self.back = ttk.Button(self, image=self.back_img,command = lambda : controller.show_frame(Page3))
		self.back.place(relx=0.05, rely=0.05)
		self.label2=ttk.Label(self, text="Receipt").place(x=122.44403076171875, y=70)
		self.label3=ttk.Label(self,text="ITEMS").place(x=25, y=92)
		self.label4=ttk.Label(self,text="QTY").place(x=130, y=100)
		self.label5=ttk.Label(self,text="PRICE").place(x=210, y=100)
		self.print_img = PhotoImage(file=relative_to_assets("print.png"))
		self.print_but= ttk.Button(self, image=self.print_img,command = lambda : controller.show_frame(Page5))
		self.print_but.place(x=110.59600830078125,y=211.510009765625)
		

class Page5(tk.Frame):
	def __init__(self, parent,controller):
		tk.Frame.__init__(self, parent)
		label_1 = ttk.Label(self,text="THANK YOU FOR RECYCLING",font=LARGEFONT)
		label_1.place(relx=0.5,rely=0.16,anchor=CENTER)
		self.back_img = PhotoImage(file=relative_to_assets("home.png"))
		self.back = ttk.Button(self,image=self.back_img, command=lambda: controller.show_frame(StartPage))
		self.back.place(relx=0.5, rely=0.92,anchor=CENTER)
		#self.qr_label = ttk.Label(self, text="Loading...")
		#self.qr_label.place(relx=0.5, rely=0.7, anchor=CENTER)
		self.load_image()
	def load_image(self):
		auth = requests.post('https://dropme.up.railway.app/user_login/', json={"email":'admin@gmail.com', 'password':'admin'})
		auth.json()
		r = requests.get('https://dropme.up.railway.app/machines/qrcode/machine/', headers={'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1Nzk0Njk3LCJpYXQiOjE2ODMyMDI2OTcsImp0aSI6IjVlZTRkMzNjYWEzZjQyYzU4ZTgwYzUzMmNjNTU4NGEwIiwidXNlcl9pZCI6MX0.mGPAiQ9WRPnjUL5P8L-J6UwJ3gzPwTtNeLFr92z_Cv4'})
		self.qr_img = Image.open(BytesIO(r.content))
		width, height = self.qr_img.size
		self.qr_img = self.qr_img.resize((int(width/2), int(height/2)))
		self.qr_photo = ImageTk.PhotoImage(self.qr_img)
		self.qr_label = ttk.Label(self, image=self.qr_photo)
		self.qr_label.place(relx=0.5, rely=0.5, anchor=CENTER)
	
		
    
if __name__ == "__main__":

    app = tkinterApp()
    app.geometry("280x400+200+0")

    
    root = tk.Toplevel(app)
    root.overrideredirect(True)    
    root.geometry("300x300+200+430")
    videoPlayer = tk.Label(root)
    videoPlayer.pack()
    file="C:\\Users\\Esraa\\Desktop\\pyy\\vid"
    video = tkvideo(file + ".mp4", videoPlayer, loop=1)
    video.play() 
    root.mainloop()
    app.mainloop() 
