
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


win = Tk()
win.geometry("750x800+400+30")

color = "#581845"
frame_1 = Frame(win, width=750, height=800, bg=color).place(x=0, y=0)
show_ind = Label(frame_1, bg="#581845", fg='white',font=('Times New Roman',20,'bold'))
show_ind.place(x=620,y=150)

#stylish rec color
colors = "Red", "Green", "Blue", "Yellow", "Black"
cmb = ttk.Combobox(frame_1, width=10, values=colors)
cmb.current(0)
cmb.place(x= 520 , y=160)

#detect colors
Colors ="Red", "Orange", "Blue","Laser","Scales"
cmb2 = ttk.Combobox(frame_1, width=10, values=Colors)
cmb2.current(2)
cmb2.place(x= 520 , y=200)
show_color = Label(frame_1, bg="#581845", fg='white',font=('Times New Roman',10,'bold'))
show_color.place(x=600,y=200)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

W = 150
l_h = Scale(frame_1, label="l_h", from_=0, to=255, orient=HORIZONTAL, variable=var1, activebackground='#339999')
l_h.set(0)
l_h.place(x=10, y=10, width=W)
l_s = Scale(frame_1, label="l_s", from_=0, to=255, orient=HORIZONTAL, variable=var2, activebackground='#339999')
l_s.set(0)
l_s.place(x=170, y=10, width=W)
l_v = Scale(frame_1, label="l_v", from_=0, to=255, orient=HORIZONTAL, variable=var3, activebackground='#339999')
l_v.set(0)
l_v.place(x=330, y=10, width=W)
##############################
u_h = Scale(frame_1, label="u_h", from_=255, to=0, orient=HORIZONTAL, variable=var4, activebackground='#339999')
u_h.set(255)
u_h.place(x=10, y=80, width=W)
u_s = Scale(frame_1, label="u_s", from_=255, to=0, orient=HORIZONTAL, variable=var5, activebackground='#339999')
u_s.set(255)
u_s.place(x=170, y=80, width=W)
u_v = Scale(frame_1, label="u_v", from_=255, to=0, orient=HORIZONTAL, variable=var6, activebackground='#339999')
u_v.set(255)
u_v.place(x=330, y=80, width=W)
################################
Area = Scale(frame_1,label="area", from_=10, to=5000, orient=VERTICAL, variable=var7, activebackground='#339999')
Area.set(300)
Area.place(x=515, y=10, height=130)


button =Button(frame_1,text="Print")

label1 = Label(frame_1)
label2 = Label(frame_1)
label3 = Label(frame_1)

co = Label(frame_1, bg="#581845", fg='white')
show_ind = Label(frame_1, bg="#581845", fg='white',font=('Times New Roman',20,'bold'))
show_ind.place(x=10,y=700)
##############
def clean():
        show_ind['text'] =""
############
clear =Button(frame_1,text="clear",command=clean)
clear.place(x=400,y=700)
################################
def to_pil(img, label, x, y, w, h):
    img = cv2.resize(img, (w, h))
    image = Image.fromarray(img)
    pic = ImageTk.PhotoImage(image)
    label.configure(image=pic)
    label.image = pic
    label.place(x=x, y=y)
################################
def LINE(rgb,startp=(100,100),endp=(120,100)):
    if cmb.get() =="Red":
        cv2.line(rgb, startp, endp, (200, 0, 0), 2)
    if cmb.get() =="Blue":
        cv2.line(rgb, startp, endp, (0, 0, 200), 2)
    if cmb.get() =="Green":
        cv2.line(rgb, startp, endp, (0, 200, 0), 2)
    if cmb.get() =="Blue":
        cv2.line(rgb, startp, endp, (0, 0, 200), 2)
    if cmb.get() =="Yellow":
        cv2.line(rgb, startp, endp, (200, 200, 0), 2)
    if cmb.get() =="Black":
        cv2.line(rgb, startp, endp, (0, 0, 0), 2)

def stylish_rec(rgb,x,y,w,h,v):
    # TOP LEFT
    LINE(rgb,(x,y),(x+v,y))
    LINE(rgb,(x,y),(x,y+v))
    #TOP RIGHT
    LINE(rgb,(x+w,y),(x+w-v,y))
    LINE(rgb,(x+w,y),(x+w,y+v))
    #BOTTOM LIFT
    LINE(rgb,(x,y+h),(x,y+h-v))
    LINE(rgb,(x,y+h),(x+v,y+h))
    #BUTTOM RIGHT
    LINE(rgb,(x+w,y+h),(x+w,y+h-v))
    LINE(rgb,(x+w,y+h),(x+w-v,y+h))
################################
b=400
def rows(rgb):
    for y in range(1,6):
        cv2.line(rgb, (100,y*70), (b,y*70), (0, 200, 0), 2)
def cols(rgb):
    for x in range(1,5):
        cv2.line(rgb, (x*100,70), (x*100,b-50), (0, 200, 0), 2)
################################
counter = 0
def show_rec(rgb,x,y,w,h):
    global counter
    col =[100,200,300,400]
    row = [70,140,220,290,360]
    index_col_one = '1','4','7','#',''
    index_col_two = '2','5','8','0',''
    index_col_three ='3','6','9','*',''
    
    #first col
    for i in range(0,4):
        cv2.putText(rgb, str(index_col_one[i]), (145, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (0, 255, 50))
        if (x+w > col[0] and x+w <col[1]) and (y+h > row[i] and y+h < row[i]+70):
            cv2.rectangle(rgb, (x, y), (x + w, y + h), (40*i, 100, 0), -1)
            if (x+w > col[0] and x+w <col[1]) and (y+h > row[i] and y+h < row[i]+70):
                counter +=1
                if counter >=30:
                    show_ind['text'] +=str(index_col_one[i])
                    cv2.putText(rgb, str(index_col_one[i]), (145, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (200, 0, 0))
                    counter = 0
            else:
                counter =0
    #second col
    for i in range(0,4):
        cv2.putText(rgb, str(index_col_two[i]), (245, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (0, 255, 50))
        if (x+w > col[1] and x+w <col[2]) and (y+h > row[i] and y+h < row[i]+70):
            cv2.rectangle(rgb, (x, y), (x + w, y + h), (0, 40, 0), -1)
            # show_ind['text'] +=str(index_col_two[i]) 
            if (x+w > col[1] and x+w <col[2]) and (y+h > row[i] and y+h < row[i]+70):
                counter +=1
                if counter >=30:
                    show_ind['text'] +=str(index_col_two[i])
                    cv2.putText(rgb, str(index_col_two[i]), (245, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (200, 0, 0))
                    counter = 0
            else:
                counter =0
           
    # third col
    for i in range(0,4):
        cv2.putText(rgb, str(index_col_three[i]), (345, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (0, 255, 50))
        if (x+w > col[2] and x+w <col[3]) and (y+h > row[i] and y+h < row[i]+70):
            cv2.rectangle(rgb, (x, y), (x + w, y + h), (0, 200, 0), -1)
            # show_ind['text'] +=str(index_col_three[i])
            if (x+w > col[2] and x+w <col[3]) and (y+h > row[i] and y+h < row[i]+70):
                counter +=1
                if counter >=30:
                    show_ind['text'] +=str(index_col_three[i])
                    cv2.putText(rgb, str(index_col_three[i]),(345, row[i]+40), cv2.FONT_HERSHEY_TRIPLEX, 0.70, (200, 0, 0))
                    counter = 0
            else:
                counter =0

    # do anything if the number has been entered      
    if show_ind['text'] =="1698":
        show_ind['text'] ="Open"
    
    
#################################  
cap = cv2.VideoCapture(0)        
def display():
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (500,500))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if cmb2.get()=="Red":
        l_b = np.array([157 , 114 , 39 ]) #red
        u_b = np.array([ 255 , 255 , 255])
    if cmb2.get()=="Blue":
        l_b = np.array([0 , 171 , 91 ]) #blue
        u_b = np.array([ 148 , 255 , 255])
    if cmb2.get()=="Orange":
        l_b = np.array([0 , 0 , 91 ]) #orange
        u_b = np.array([ 100 , 255 , 248])
    if cmb2.get()=="Laser":
        l_b = np.array([0 , 0 , 255 ]) #laser
        u_b = np.array([ 255 , 255 , 255])
    if cmb2.get()=="Scales":
        l_b = np.array([l_h.get(), l_s.get(), l_v.get()])
        u_b = np.array([u_h.get(), u_s.get(), u_v.get()])
        button.place(x=700,y=10)
        button['command']=lambda:print(l_h.get(), ',', l_s.get(), ',', l_v.get(), ',', u_h.get(), ',', u_s.get(), ',', u_v.get())
    else:
        button.place_forget()
    show_color['text']="Tracking "+cmb2.get()+" Color"

    cols(rgb) # HORIZONTAL lines
    rows(rgb) # VERTICAL lines

    mask = cv2.inRange(hsv, l_b, u_b)
    kernal = np.ones((5, 5), "uint8")
    color = cv2.dilate(mask, kernal)
    res = cv2.bitwise_and(img, img, mask=mask)
    rgb2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    contours, _ = cv2.findContours(color, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > Area.get():
            x, y, w, h = cv2.boundingRect(contour)
            stylish_rec(rgb,x,y,w,h,10)
            show_rec(rgb,x,y,w,h)

            co['text'] = 'y= ' + str(int(y)) + '\n' + 'x= ' + str(int(x))
            co.place(x=540, y=600)

    to_pil(rgb, label1, 10, 160,500,500)
    to_pil(rgb2, label2, 520, 250, 200, 160)
    to_pil(mask, label3, 520, 420, 200, 160)
    win.after(20, display)

display()
win.mainloop()