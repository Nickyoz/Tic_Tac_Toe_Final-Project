#Imports the tools we need for the game
from tkinter import *
from tkinter import messagebox
import random as r

#Defining the button actions for the game such as the structures and placement od the X's and O's
def button(frame):         
    b=Button(frame,padx=1,width=3,text="   ")
    return b
def change_a():             
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
#Resets the map when starting a new game
def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
#Displays the winner/tie window when the results are in
def check():                
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("'"+a+"' has won")
                    reset()
    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("'"+a+"' has won")
        reset()   
    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("It is draw")
        reset()
def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=color[a])
        check()
        change_a()
        label.config(text=a+"'s turn")
#Defining the window layout
root=Tk()                  
root.title("Tic Tac Toe")   
a=r.choice(['O','X'])      
color={'O':"black",'X':"black"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)
label=Label(text=a+"'s turn")
label.grid(row=3,column=0,columnspan=3)
 
root.mainloop()
