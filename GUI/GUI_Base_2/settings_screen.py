from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from PIL import ImageTk, Image
import string


class settings_screen(Frame):
    def __init__(self, master=None, dict_object=None, user="User 1", super_master=None, start_up=False, template_exists=False):
        Frame.__init__(self, master)        
        self.master = master        
        self.colors = self.master.colors
        self.config(bg=self.colors["bg"])
        self.fonts = self.master.fonts
        self.master.title("Graph Adjacency Matrix")
        self.matrix = {}
        self.column_A = Frame(self, background=self.colors["bg"])
        self.f1 = LabelFrame(self.column_A, text="Adjacency Matrix", font=self.fonts["text"], relief=RAISED, padx=5, pady=5, bg=self.colors["panel_1"], fg=self.colors["text_1"])
        self.saved = False

        alphabets = string.ascii_uppercase
         
        counter = 0
        for row in range(self.master.dict["nodes"] + 1):
            for col in range(self.master.dict["nodes"] + 1):
                if(row > 0 and col > 0):
                    self.matrix[counter] = Entry(self.f1, width=15, font=self.fonts["text"], disabledbackground=self.colors["ia_bg"])
                    self.matrix[counter].insert(0, '0')
                    self.matrix[counter].grid(row=row, column=col, pady=2)
                    counter+=1
                elif(row == 0):
                    if(col == 0):
                        Label(self.f1, text="", width=15, anchor="center", font=self.fonts["text"], bg=self.colors["panel_1"], fg=self.colors["text_1"]).grid(row=0, column=0, sticky=W)
                    else:
                        Label(self.f1, text=str(alphabets[col - 1]), width=15, anchor="center", font=self.fonts["text"], bg=self.colors["panel_1"], fg=self.colors["text_1"]).grid(row=row, column=col, sticky=W)
                elif(col == 0):
                    Label(self.f1, text=str(alphabets[row - 1]), width=15, anchor="e", font=self.fonts["text"], bg=self.colors["panel_1"], fg=self.colors["text_1"]).grid(row=row, column=col, sticky=W)
        
        self.f1.grid(row=0, column=0, rowspan=7, pady=10)
        self.column_A.grid(row=0, column=0, padx=10, pady=10, sticky="N")
       
        self.button_frame = Frame(self, bg=self.colors["bg"])
        
        self.b_back = Button(self.button_frame, text="Back", font=self.fonts["bold"], command=self.goback, bg="white", fg=self.colors["blue"])
        self.b_save = Button(self.button_frame, text="Save", font=self.fonts["bold"], command=self.save_all_settings, bg="white", fg=self.colors["blue"]) 
        self.b_visualize = Button(self.button_frame, text="Visualize", font=self.fonts["bold"], command=self.visualize, bg="white", fg=self.colors["blue"])
        self.b_ex = Button(self.button_frame, text="Exit", font=self.fonts["bold"], command=self.exit_callback, bg="white", fg=self.colors["blue"])
               

        self.b_back.pack(padx=20, pady=20, side=LEFT)
        self.b_save.pack(padx=20, pady=20, side=LEFT)
        self.b_visualize.pack(padx=20, pady=20, side=LEFT)
        self.b_ex.pack(padx=20, pady=20, side=LEFT)
        
        self.button_frame.grid(row=2, column=0, columnspan=3)

    def goback(self):
        self.master.show_startup_screen()

    def visualize(self):
        if(self.saved):
            self.master.show_visual_screen()
        else:
            messagebox.showerror("Error!!","Please save first!!")
            return False

    def exit_callback(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quit()
            self.destroy()
    
    def save_all_settings(self):
        self.new_matrix = []
        
        for counter in range(self.master.dict["nodes"] ** 2):
            if(int(self.matrix[counter].get()) == 0 or int(self.matrix[counter].get()) == 1):
                self.new_matrix.append(int(self.matrix[counter].get()))
            else:
                messagebox.showerror("Error!!","Please check that the values in matrix are 1 or 0!")
                return False  
        self.new_matrix_array = np.array(self.new_matrix).reshape(self.master.dict["nodes"], self.master.dict["nodes"])
        self.master.dict["matrix"] = self.new_matrix_array
        self.saved = True                  
        return True
    

    

        
