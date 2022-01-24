from tkinter import *
import tkinter.font as font
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import messagebox
import networkx as nx
from PIL import ImageTk, Image
from networkx.drawing.nx_agraph import graphviz_layout
import string


class visual_screen(Frame):
    

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.colors = self.master.colors
        self.fonts = self.master.fonts
        self.configure(bg=self.colors["bg"])

        self.s = ttk.Style()
        self.s.configure('my.TButton', bordercolor=self.colors["red_2"], font=self.fonts["bold"], foreground=self.colors["red_2"], background="white")

        self.configure(highlightbackground="black", highlightthickness=2)
        arr = self.master.dict["matrix"]
        G = nx.Graph()

        fixed_lst = [(0.5 + 0.0,0.5 + 0.0) , (0.5 + 0.1,0.5 + 0.1) , (0.5 - 0.1,0.5 + 0.1) , (0.5 + 0.1,0.5 - 0.1) , (0.5 - 0.1,0.5 - 0.1),
                     (0.5 + 0.2,0.5 + 0.2) , (0.5 - 0.2,0.5 + 0.2) , (0.5 + 0.2,0.5 - 0.2) , (0.5 - 0.2,0.5 - 0.2),
                     (0.5 + 0.3,0.5 + 0.3) , (0.5 - 0.3,0.5 + 0.3) , (0.5 + 0.3,0.5 - 0.3) , (0.5 - 0.3,0.5 - 0.3),
                     (0.5 + 0.4,0.5 + 0.4) , (0.5 - 0.4,0.5 + 0.4) , (0.5 + 0.4,0.5 - 0.4) , (0.5 - 0.4,0.5 - 0.4),
                     (0.5 + 0.5,0.5 + 0.5) , (0.5 - 0.5,0.5 + 0.5) , (0.5 + 0.5,0.5 - 0.5) , (0.5 - 0.5,0.5 - 0.5),
                     (0.5 + 0.6,0.5 + 0.6) , (0.5 - 0.6,0.5 + 0.6) , (0.5 + 0.6,0.5 - 0.6) , (0.5 - 0.6,0.5 - 0.6),
                     (0.5 + 0.7,0.5 + 0.7)]
        fixed_positions = {}
        labeldict = {}
        alphabets = string.ascii_uppercase
        size = self.master.dict["nodes"]
        tup = []
        for row in range(1, size + 1):
            labeldict[row] = str(alphabets[row - 1])
            fixed_positions[row] = fixed_lst[row - 1]
        for row in range(1, size + 1):
            G.add_node(alphabets[row -1], pos = fixed_lst[row - 1])  
        for row in range(1, size + 1):
            for col in range(1, size + 1):
                if(arr[row - 1][col - 1] == 1):
                    if(alphabets[row - 1] == alphabets[col -1]):
                        G.add_edge(alphabets[row - 1], alphabets[col -1])
                        tup.append((alphabets[row - 1], alphabets[col -1]))
                    else:
                        G.add_edge(alphabets[row - 1], alphabets[col -1])
        
        G.to_undirected()
        fixed_nodes = fixed_positions.keys()
        edges = G.edges()

        self.button_frame = Frame(self, bg=self.colors["bg"])
        
        self.b_home = Button(self.button_frame, text="Home", font=self.fonts["bold"], command=self.gohome, bg="white", fg=self.colors["blue"])
        self.b_set = Button(self.button_frame, text="Settings", font=self.fonts["bold"], command=self.goset, bg="white", fg=self.colors["blue"]) 
        self.b_exit = Button(self.button_frame, text="Exit", font=self.fonts["bold"], command=self.exit_callback, bg="white", fg=self.colors["blue"])
               

        self.b_home.pack(padx=20, pady=20, side=LEFT)
        self.b_set.pack(padx=20, pady=20, side=LEFT)
        self.b_exit.pack(padx=20, pady=20, side=LEFT)

        self.button_frame.pack()

        self.res = nx.is_tree(G)
        if(self.res):
            self.display = "~* The graph of the provided adjacency matrix is a Tree *~"
        else:
            self.display = "~* The graph of the provided adjacency matrix is a NOT a Tree *~"

        self.resultFrame = Frame(self, bg=self.colors["title_bg"])  
        if(self.res):     
            self.labl = Label(self.resultFrame, text=self.display, font=self.fonts["bold"], pady=10, bg=self.colors["panel_1"], fg="lightgreen") 
        else:
            self.labl = Label(self.resultFrame, text=self.display, font=self.fonts["bold"], pady=10, bg=self.colors["panel_1"], fg="red") 
        self.labl.pack(side=TOP, pady=0, expand=True, fill=X, anchor=S)
        self.resultFrame.pack(side=TOP, expand=True, fill=X, anchor=S)
            

        

        
        fr = Frame(self, relief=RAISED, borderwidth=0, bg=self.colors["panel_1"])
        fr.pack(side = TOP, fill = BOTH, expand = 1)

        fig = plt.figure(figsize=(14.9,6))
        canvas = FigureCanvasTkAgg(fig, master=fr) 
        canvas.draw()
        toolbar = NavigationToolbar2Tk(canvas, fr)
        toolbar.update()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        a = fig.add_subplot(111)
        a.cla()
        a.set_xlim(0.25,0.75)
        a.set_ylim(0.25,0.75)
        layout = dict((n, G.nodes[n]["pos"]) for n in G.nodes())
        nx.draw_networkx_nodes(G, pos=layout, nodelist = G.nodes(), node_size = 100, node_color = 'green', alpha = 0.6)
        nx.draw_networkx_labels(G, pos=layout, font_size = 7, font_color = "blue", alpha = 0.6)
        nx.draw_networkx_edges(G, pos=layout, edgelist = tup, edge_color = 'r', style = 'solid', alpha = 0.6)
        ax = plt.gca()
        for edge in edges:
            ax.annotate("",
                    xy=layout[edge[0]], xycoords='data',
                    xytext=layout[edge[1]], textcoords='data',
                    arrowprops=dict(arrowstyle="-",color='r',alpha = 0.6, 
                                    shrinkA=2, shrinkB=2,
                                    patchA=None, patchB=None,
                                    connectionstyle="arc3,rad=-0.3",
                                    ),
                        )
        plt.axis('off')
        canvas.draw()

        

    def gohome(self):
        self.master.show_startup_screen()

    def goset(self):
        self.master.show_settings_screen()

    def exit_callback(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.quit()
            self.destroy()


        
    def isCyclicUtil(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, v) == True:
                    return True
            elif i != parent:
                return True
 
        return False
    def isaTree(self):
        visited = [False] * self.V
        if self.isCyclicUtil(0, visited, -1) == True:
            return False
 
        for i in range(self.V):
            if visited[i] == False:
                return False
 
        return True
