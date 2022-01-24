from tkinter import *
from tkinter import ttk
import tkinter.font as font
import tkinter as tk
from settings_screen import settings_screen
from tkinter import messagebox  
from PIL import ImageTk, Image

class startup_screen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.colors = self.master.colors
        self.fonts = self.master.fonts
        IMAGE_PATH = 'images\\bg.jpg'
        WIDTH, HEIGTH = self.master.wmax, self.master.hmax
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGTH-150, bd=0, highlightthickness=0)
        self.s = ttk.Style()
        self.s.theme_use('clam')
        self.s.configure('my.TButton', bordercolor=self.colors["blue"], font=self.fonts["bold"], foreground=self.colors["blue"], background="white")


        img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        self.canvas.background = img 
        bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        self.canvas.pack(fill=BOTH, expand=True)        

        self.loginFrame = Frame(self, bg='#ab9a86')
        
        self.user_new = Entry(self, width=20, font=self.fonts["subtitle"], fg="#555555", highlightthickness=2)
        self.user_new.insert(0, self.master.dict["User"])
        self.user_new.bind('<FocusIn>', self.get_uid_input)
        self.user_new.configure(highlightbackground="blue")

        self.pwd_new = Entry(self, width=20, font=self.fonts["subtitle"], fg="#555555", highlightthickness=2)
        self.pwd_new.insert(0, self.master.dict["nodes"])
        self.pwd_new.bind('<FocusIn>', self.get_pwd_input)   
        self.pwd_new.configure(highlightbackground="blue")
        
        self.btn1 = ttk.Button(self, style="my.TButton", text="Login", command=self.check_credentials)

        self.w_1 = self.canvas.create_window(WIDTH/2, 300, anchor=CENTER, window=self.user_new)
        self.w_2 = self.canvas.create_window(WIDTH/2, 350, anchor=CENTER, window=self.pwd_new)
        self.w_3 = self.canvas.create_window(WIDTH/2, 420, anchor=CENTER, window=self.btn1)


    def check_credentials(self):
        """Validate login credentials"""
        WIDTH, HEIGTH = self.master.wmax, self.master.hmax        
        u_n = self.user_new.get()
        self.master.dict["User"] = u_n
        p_wd = self.pwd_new.get()
        self.master.dict["nodes"] = int(p_wd)
        valid = True
        if valid:
            self.master.switch_frame(settings_screen)
            messagebox.showinfo("Welcome!", "Welcome to the program " + str(u_n) + "\nPlease enter the matrix!")
        else:
            self.canvas.create_text(WIDTH/2, 500, text="Incorrect Username or Password !!", font=("Helvetica", 12), fill="red")

    def get_uid_input(self, x):
        self.user_new.delete(0, 'end')
        self.user_new.config(fg="#000000")

    def get_pwd_input(self, x):
        self.pwd_new.delete(0, 'end')
        self.pwd_new.config(fg="#000000")
