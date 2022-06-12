import random
from tkinter import *
import sys
from tkinter import messagebox
from random import choice
ty=Tk()


ty.geometry("380x300")
#ty.config(bg="teal")
ty.config(padx=20,pady=30,bg="teal")
#this geometry widgets is used to set the window size(width=  ,height=)
canvas=Canvas(width=456,height=450)
#used to make the background color and the canvas width around
canvas.configure(bg="white",highlightthickness=0)
 # CHECKING TO SEE IF SOMEONE HAS WON OR NOT..
def reset_buttons():
   global b1,b2,b3,b4,b5,b6,b7,b8,b9
   b1 = Button(ty, text=" ", bg="black", borderwidth=0, command=lambda: b_click(b1))
   b1.place(x=0, y=0, width=120, height=78)
   b2 = Button(ty, text=" ", command=lambda: b_click(b2), bg="black", highlightthickness=0, borderwidth=0)
   b2.place(x=0, y=82, width=120, height=76)
   b3 = Button(ty, text=" ", command=lambda: b_click(b3), bg="black", highlightthickness=0, borderwidth=0)
   b3.place(x=0, y=163, width=120, height=76)
   b4 = Button(ty, text=" ", command=lambda: b_click(b4), bg="black", highlightthickness=0, borderwidth=0)
   b4.place(x=126, y=163, width=100, height=76)
   b5 = Button(ty, text=" ", command=lambda: b_click(b5), bg="black", highlightthickness=0, borderwidth=0)
   b5.place(x=126, y=83, width=100, height=75)
   b6 = Button(ty, text=" ", command=lambda: b_click(b6), bg="black", highlightthickness=0, borderwidth=0)
   b6.place(x=126, y=0, width=100, height=78)
   b7 = Button(text=" ", command=lambda: b_click(b7), bg="black", highlightthickness=0, borderwidth=0)
   b7.place(x=232, y=163, width=108, height=76)
   b8 = Button(ty, text=" ", command=lambda: b_click(b8), bg="black", highlightthickness=0, borderwidth=0)
   b8.place(x=232, y=83, width=108, height=75)
   b9 = Button(ty, text=" ", command=lambda: b_click(b9), bg="black", highlightthickness=0, borderwidth=0)
   b9.place(x=232, y=0, width=108, height=77)

def disable_buttons():
   b1.config(state=DISABLED)
   b2.config(state=DISABLED)
   b3.config(state=DISABLED)
   b4.config(state=DISABLED)
   b5.config(state=DISABLED)
   b6.config(state=DISABLED)
   b7.config(state=DISABLED)
   b8.config(state=DISABLED)
   b9.config(state=DISABLED)

def won():
   if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
      b1.config(fg="red")
      b2.config(fg="red")
      b3.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1  WON ")
      disable_buttons()
   elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
      b4.config(fg="red")
      b5.config(fg="red")
      b6.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1  WON ")
      disable_buttons()
   elif b8["text"]=="X" and b7["text"]=="X" and b9["text"]=="X":
      b7.config(fg="red")
      b8.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1   WON ")
      disable_buttons()
   elif b1["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
      b1.config(fg="red")
      b5.config(fg="red")
      b7.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1   WON ")
      disable_buttons()
   elif b3["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
      b3.config(fg="red")
      b5.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1   WON ")
      disable_buttons()
   elif b1["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" :
      b1.config(fg="red")
      b6.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!!  Player1  WON ")
      disable_buttons()
   elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" :
      b2.config(fg="red")
      b5.config(fg="red")
      b8.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player1  WON ")
      disable_buttons()
   elif b3["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" :
      b3.config(fg="red")
      b4.config(fg="red")
      b7.config(fg="red")
      messagebox.showinfo("TIC TAC TOE" , message="Congrats!! Player1 WON ")
      disable_buttons()
   elif b1["text"]=="0" and b2["text"]=="0" and b3["text"]=="0"  :
      b1.config(fg="red")
      b2.config(fg="red")
      b3.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b4["text"]=="0" and b5["text"]=="0" and b6["text"]=="0" :
      b4.config(fg="red")
      b5.config(fg="red")
      b6.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b8["text"]=="0" and b7["text"]=="0" and b9["text"]=="0":
      b7.config(fg="red")
      b8.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b1["text"]=="0" and b5["text"]=="0" and b7["text"]=="0":
      b1.config(fg="red")
      b5.config(fg="red")
      b7.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b3["text"]=="0" and b5["text"]=="0" and b9["text"]=="0":
      b3.config(fg="red")
      b5.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif  b1["text"]=="0" and b6["text"]=="0" and b9["text"]=="0" :
      b1.config(fg="red")
      b6.config(fg="red")
      b9.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b2["text"]=="0" and b5["text"]=="0" and b8["text"]=="0" :
      b2.config(fg="red")
      b5.config(fg="red")
      b8.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()
   elif b3["text"]=="0" and b4["text"]=="0" and b7["text"]=="0" :
      b3.config(fg="red")
      b4.config(fg="red")
      b7.config(fg="red")
      messagebox.showinfo("TIC TAC TOE", message="Congrats!! Player2 WON ")
      disable_buttons()

 #  INSERTING THE X AND 0 IN ONE CLICK..
clicked=True    # used for the conditions
count=0    # used for the conditions
def b_click(b):
   global clicked,count
   #the global keyword is used inside the function so that we can call the value of that global variable inside the func.
   if b["text"]==" " and clicked==True:
      b.config(text="X", font=("courier new" , 50 ,"bold",) ,fg="white")
      clicked=False
      count+=1
      won()
   elif b["text"]==" " and clicked==False:
      clicked=True
      b.config(text="0", font=("courier new", 50, "bold"), fg="white")
      count+=1
      won()
   else:
      messagebox.showinfo("TIC TAC TOE", message="hey! that box has alreday being filled")

canvas.create_line(1,80,500,80,fill="white",width=2)
#used to create the line & passes arguemnts(x1,y1,x2,y2,border width)
#this widget is for the drawing the line within the coordinates..x1 and y1 are the starting point and x2 and y2 are the end point to finish the line

canvas.create_line(230,0,230,450,fill="white",width=3)
canvas.create_line(125,0,125,450,fill="white",width=3)
canvas.create_line(1,160,450,160,fill="white",width=3)
canvas.pack()
b1 = Button(ty,text=" ",bg="black", borderwidth=0, command=lambda: b_click(b1) )
b1.place(x=0,y=0,width=120,height=78 )
b2=Button(ty,text=" ",command=lambda: b_click(b2),bg="black",highlightthickness=0,borderwidth=0)
b2.place(x=0,y=82,width=120,height=76 )
b3=Button(ty,text=" ",command=lambda:b_click(b3),bg="black",highlightthickness=0,borderwidth=0)
b3.place(x=0,y=163,width=120,height=77)
b4=Button(ty,text=" ",command=lambda: b_click(b4),bg="black",highlightthickness=0,borderwidth=0)
b4.place(x=126,y=163,width=100,height=77)
b5=Button(ty,text=" ",command=lambda:b_click(b5),bg="black",highlightthickness=0,borderwidth=0)
b5.place(x=126,y=83,width=100,height=75)
b6=Button(ty,text=" ",command=lambda:b_click(b6),bg="black",highlightthickness=0,borderwidth=0)
b6.place(x=126,y=0,width=100,height=78)
b7=Button(text=" ",command=lambda:b_click(b7),bg="black",highlightthickness=0,borderwidth=0)
b7.place(x=232,y=163,width=108,height=77)
b8=Button(ty,text=" ",command=lambda:b_click(b8),bg="black",highlightthickness=0,borderwidth=0)
b8.place(x=232,y=83,width=108,height=75)
b9=Button(ty,text=" ",command=lambda:b_click(b9),bg="black",highlightthickness=0,borderwidth=0)
b9.place(x=232,y=0,width=108,height=77)
#create menue at the top corner
menu_lol=Menu(ty)
# we are passing the "ty" to put this menu inside the window and ty is the variable that defines the window..
ty.config(menu=menu_lol)
menu_lol.add_command(label="Reset", command=reset_buttons)
menu_lol.add_command(label="Quit!", command=exit)


#create options menu






ty.mainloop()