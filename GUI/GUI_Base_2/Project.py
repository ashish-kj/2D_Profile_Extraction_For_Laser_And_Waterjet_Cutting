import tkinter as tk
from tkinter import *
from startup_screen import startup_screen
from settings_screen import settings_screen
from visual_screen import visual_screen
import os
import numpy as np
import tkinter.font as font
from PIL import ImageTk, Image
from win32api import GetMonitorInfo, MonitorFromPoint

class Project(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.colors = {            
            "blue"      : "#007dbd",
            "bg"        : "#4b5e6c",
            "panel_1"   : "#313c4c",          
            "panel_2"   : "#394264",
            "panel_3"   : "#394264",
            "green"     : "#11a8ab",
            "red_1"     : "#e64c65",
            "red_2"     : "#cc324b",
            "text_1"    : "#FFFFFF",
            "text_2"    : "#000000",
            "gray"      : "#777777",
            "window_bg" : "#FFFFFF",            
            "frame_bg"  : "#6d6ab0",
            "warning_bg": "#e64c65",
            "title_bg"  : "#c8c1e7",
            "ia_bg"     : "#DDDDDD",
            "active_bg" : "#FFFFFF",
            "blue_font" : "#004976",
        }		        
        self.config(bg=self.colors["bg"])
        self.fonts = {
            "text"      : font.Font(family="Verdana", size=11),
            "title"     : font.Font(family="Verdana", size=18),
            "subtitle"  : font.Font(family="Verdana", size=12),
            "small"     : font.Font(family="Verdana", size=10),
            "bold"      : font.Font(family="Verdana", size=11, weight="bold"),
        }
        self.state('zoomed') 
        self.title("Discrete Structures Assignment")
        self.iconImage = PhotoImage(file="images\\logo.png")
        self.iconphoto(False, self.iconImage)
        monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
        self.work_area = monitor_info.get("Work")
        self.wmax = self.work_area[2]
        self.hmax = self.work_area[3]
        self.dict = {}
        self.dict["User"] = "Enter User Name"
        self.dict["nodes"] = "Number of nodes"
        self.startup_frame  = None
        self.settings_frame = None
        self.visual_frame     = None
        self.done =0

        self.title_frame    = Frame(self, bg=self.colors["panel_1"],)
        self.myImage        = ImageTk.PhotoImage(Image.open("images\\logo.png").resize([85,85]))
        self.imageLabel     = Label(self.title_frame, image=self.myImage, bg=self.colors["panel_1"],)
        self.imageLabel.pack(side=LEFT)
        self.label_title    = Label(self.title_frame, text="Discrete Structures Assignment", bg=self.colors["panel_1"], fg=self.colors["text_1"], font=self.fonts["title"], padx=20, pady=2)
        self.label_subtitle = Label(self.title_frame, text="Please wait while program starts up...", bg=self.colors["panel_1"], fg=self.colors["text_1"],
                                    font=self.fonts["subtitle"], padx=20, pady=2)
        self.label_title.pack(side=TOP, fill=X, expand=YES)
        self.label_subtitle.pack(side=TOP, fill=X, expand=YES)
        self.title_frame.pack(side=TOP, fill=X)
        self.switch_frame(startup_screen)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        if self.startup_frame is not None:
            self.startup_frame.pack_forget()
        if self.settings_frame is not None:
            self.settings_frame.pack_forget()
        if self.visual_frame is not None:
            self.visual_frame.pack_forget()
        self.update()
        if frame_class is startup_screen:
            if self.startup_frame is None:
                self.startup_frame = startup_screen(self)
                self.startup_frame.pack(side=TOP, fill=NONE, anchor=CENTER, expand=True)
                self.startup_frame.tkraise()    

            else:
                for widget in self.startup_frame.winfo_children():
                    widget.destroy()
                self.startup_frame = startup_screen(self)
                self.startup_frame.pack(side=TOP, fill=NONE, anchor=CENTER, expand=True)
                self.startup_frame.tkraise()
            self.label_subtitle.config(text="Task: Given the adjacency matrix of an undirected simple graph, determine whether the graph is a tree.")
            self.startup_frame.update()
            if self.done == 0:
                self.copyrightFrame = Frame(self, bg=self.colors["title_bg"])        
                self.lbl = Label(self.copyrightFrame, text="Made by:- Anurag (2020A7PS0128U), Fazal (2020A7PS0146U) and Kartikya (2020A7PS0206U)", font=self.fonts["bold"], pady=10, bg=self.colors["panel_1"], fg=self.colors["text_1"]) 
                self.lbl.pack(side=BOTTOM, pady=0, expand=True, fill=X, anchor=S)
                self.copyrightFrame.pack(side=BOTTOM, expand=True, fill=X, anchor=S)
                self.done = 1

        if frame_class is settings_screen:
            if self.settings_frame is None:
                self.settings_frame = settings_screen(self)
                self.settings_frame.pack(side=TOP, fill=NONE, anchor=CENTER)
                self.settings_frame.tkraise()
            else:
                for widget in self.settings_frame.winfo_children():
                    widget.destroy()
                self.settings_frame = settings_screen(self)
                self.settings_frame.pack(side=TOP, fill=NONE, anchor=CENTER)
                self.settings_frame.tkraise()
            self.label_subtitle.config(text="Adjacency Matrix")
            self.state("zoomed")

        if frame_class is visual_screen:
            if self.visual_frame is None:
                self.visual_frame = visual_screen(self)
                self.visual_frame.pack(side=TOP, fill=NONE, anchor=CENTER)
                self.visual_frame.tkraise()
            else:
                for widget in self.visual_frame.winfo_children():
                    widget.destroy()
                self.visual_frame = visual_screen(self)
                self.visual_frame.pack(side=TOP, fill=NONE, anchor=CENTER)                
                self.visual_frame.tkraise()
            self.label_subtitle.config(text="Graph Visualisation")
            self.state("zoomed")

    def show_startup_screen(self):
        self.switch_frame(startup_screen)

    def show_visual_screen(self):
        self.switch_frame(visual_screen)

    def show_settings_screen(self):
        self.switch_frame(settings_screen)

if __name__ == "__main__":
    app = Project()
    app.mainloop()
