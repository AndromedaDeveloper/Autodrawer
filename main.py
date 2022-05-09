from cProfile import label
import tkinter
from turtle import *
from tkinter import *
from tkinter import filedialog
app=tkinter.Tk()
app.title('Auto Drawer')
app.geometry('500x500')
l12=Label(app, text='Auto Generated Shapes')
l12.pack()
def star():
 star12=Canvas(app)
 star12.pack()
 Screen()
 speed('fast')
 bgcolor('black')
 color('white')
 begin_fill()
 while True:
   forward(200)
   left(170)
   if abs(pos()) < 1:
        break
        end_fill()
        Screen.mainloop()
b1=Button(app,text='Star',command=star)
b1.pack()
def square():
    square12=Canvas(app)
    square12.pack()
    Screen()
    bgcolor('black')
    color('white')
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    right(90)
    forward(90)
    Screen.mainloop()
b2=Button(app,text='Square',command=square)
b2.pack()
def line():
    line12=Canvas(app)
    line12.pack()
    Screen()
    speed('normal')
    bgcolor('black')
    color('white')
    forward (90)
    Screen.mainloop()
b3=Button(app,text='Line',command=line)
b3.pack()
def back():
    back=Canvas(app)
    back.pack()
    Screen()
    bgcolor('black')
    color('white')
    forward(1)
    backward(90)
    forward(1)
    Screen.mainloop()
b4=Button(app,text='Move cursor behind the line',command=back)
b4.pack()
def delete():
    delete12=Canvas(app)
    delete12.pack()
    Screen()
    bgcolor('black')
    color('black')
    backward(90)
    Screen.mainloop()
b5=Button(app,text='Delete last straight line',command=delete)
b5.pack()
def curveheart(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        right(1)
        forward(1)
def heart():
    heart12=Canvas(app)
    heart12.pack()
    Screen()
    bgcolor('black')
    color('white')
    fillcolor('red')
    begin_fill()
    left(140)
    forward(113)
    curveheart() # Left Curve
    left(120)
    curveheart() # Right Curve
    forward(112)
    end_fill()
    Screen.mainloop()
b6=Button(app,text='Heart',command=heart)
b6.pack()
def bolt():
 bolt12=Canvas(app)
 bolt12.pack()
 Screen()
 bgcolor("black")
 color("white")
 penup()
 right(110)
 pendown()
 begin_fill()
 forward(60)
 left(90)
 forward(50)
 right(100)
 forward(60)
 left(160)
 forward(80)
 left(110)
 forward(70)
 right(90)
 forward(40)
 left(90)
 forward(20)
 end_fill()
 Screen.mainloop()
b7=Button(app, text='Bolt',command=bolt)
b7.pack()
#END OF AUTO GENERATED SHAPES

l122=Label(app,text='Advanced Options')
l122.pack()
def penup35():
    penup12=Canvas(app)
    penup12.pack()
    Screen()
    penup()
    Screen.mainloop()
b8=Button(app,text='Pen Up',command=penup35)
b8.pack()
def pendown35():
    pendown12=Canvas(app)
    pendown12.pack()
    Screen()
    pendown()
    Screen.mainloop()
b9=Button(app,text='Pen Down',command=pendown35)
b9.pack()
b10=Button(app,text='Line',command=line)
b10.pack()
def turnleft35():
    turnleft12=Canvas(app)
    turnleft12.pack()
    Screen()
    left(90)
    Screen.mainloop()
b11=Button(app,text='Turn Left by 90 Degrees',command=turnleft35)
b11.pack()
def turnright35():
    turnright12=Canvas(app)
    turnright12.pack()
    Screen()
    right(90)
    Screen.mainloop()
def backwardsa():
    backardsa12=Canvas(app)
    backardsa12.pack()
    Screen()
    right(180)
    Screen.mainloop()
b13=Button(app,text='Backwards',command=backwardsa)
b13.pack()
b12=Button(app,text='Turn Right by 90 Degrees',command=turnright35)
b12.pack()
def txteditor():
    # functions 
    def openFile():
        tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/", 
            title="Open Text file", 
            filetypes=(("Text Files", "*.txt"),)
            )
        pathh.insert(END, tf)
        tf = open(tf)
        file_cont = tf.read()
        txtarea.insert(END, file_cont)
    
        tf.close()

    ws = Tk()
    ws.title("PythonGuides")
    ws.geometry("400x500")
    ws['bg']='#2a636e'

    # adding frame
    frame = Frame(ws)
    frame.pack(pady=20)

    # adding scrollbars 
    ver_sb = Scrollbar(frame, orient=VERTICAL )
    ver_sb.pack(side=RIGHT, fill=BOTH)

    hor_sb = Scrollbar(frame, orient=HORIZONTAL)
    hor_sb.pack(side=BOTTOM, fill=BOTH)

    # adding writing space
    txtarea = Text(frame, width=40, height=20)
    txtarea.pack(side=LEFT)

    # binding scrollbar with text area
    txtarea.config(yscrollcommand=ver_sb.set)
    ver_sb.config(command=txtarea.yview)

    txtarea.config(xscrollcommand=hor_sb.set)
    hor_sb.config(command=txtarea.xview)

    # adding path showing box
    pathh = Entry(ws)
    pathh.pack(expand=True, fill=X, padx=10)

    # adding buttons 
    Button(
        ws, 
        text="Open File", 
        command=openFile
        ).pack(side=LEFT, expand=True, fill=X, padx=20)



    Button(
        ws, 
        text="Exit", 
        command=lambda:ws.destroy()
        ).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)

    ws.mainloop()
texteditorbutton=Button(app,text='Open Text Editor',command=txteditor)
texteditorbutton.pack()
#Pack the bottom label
l1=Label(app,text='Sometimes the app might crash. If this happens, restart the program.\n The drawing Panel can be only used once after a launch. If closed, restart the program. \n For any problems of your in-app experience,\n contact us at info.andromedadevelopers@yahoo.com \n Proudly made by Andromeda Developers')
l1.pack(side='bottom')
app.mainloop()