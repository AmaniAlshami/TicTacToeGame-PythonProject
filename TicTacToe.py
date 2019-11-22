import tkinter
from tkinter import messagebox

top = tkinter.Tk()
top.title("Tic Tac Toc")
Lab = tkinter.Label(top,text="Welcome to Tic Tac Toe game").grid(row=0,column=0,columnspan=3,sticky="ew")

# main function
player1 = True
def place_marker(button):
        global player1 
        if button["text"]=="" and  player1==True:
            marker="X"
            button.configure(text=marker)
            if win_check(marker):
               messagebox.showinfo("Win", " X wins ")
               play_agin()
            elif full():
                messagebox.showinfo("Win", "No one wins ! ")
                play_agin()
            player1=False
        elif button["text"]=="" and player1==False:
            marker="O" 
            button.configure(text=marker)
            if win_check(marker):
               messagebox.showinfo("Win", " O wins ")
               play_agin()
            elif full():
                messagebox.showinfo("Win", "No one wins ! ")
                play_agin()
            player1=True


def play_agin():
     message = messagebox.askquestion("Play agin","are you want to play agin?")
     if message == "yes":
        but0["text"]= but1["text"]= but2["text"]= but3["text"]= but4["text"]= but5["text"]= but6["text"]= but7["text"]= but8["text"]=""
     else :
         top.destroy()
# To restart the game
def Restart():
    message = messagebox.askquestion('Restart','Are you sure you want to restart the game?')
    global game
    if message == 'yes':
       game=True
       but0["text"]=but1["text"]=but2["text"]=but3["text"]=but4["text"]=but5["text"]=but6["text"]=but7["text"]=but8["text"]=""

def win_check(mark):
        return (but0["text"] == but1["text"] == but2["text"] == mark or # across the top
    but3["text"] == but4["text"] == but5["text"] == mark or # across the middle
    but6["text"] == but7["text"] == but8["text"] == mark or # across the bottom
    but0["text"] == but3["text"] == but6["text"] == mark or # down the middle
    but1["text"] == but4["text"] == but7["text"] == mark or # down the middle
    but2["text"] == but5["text"] == but8["text"] == mark or # down the right side
    but0["text"] == but4["text"] == but8["text"] == mark or # diagonal
    but2["text"] == but4["text"] == but6["text"] == mark)  # diagonal

def full():
   return(but0["text"]!="" and but1["text"]!="" and but2["text"]!="" and 
   but3["text"]!="" and but4["text"]!="" and but5["text"]!="" and 
   but6["text"]!="" and but7["text"]!="" and but8["text"]!="")



# Buttons
but0 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but0))
but0.grid(row=1,column=0) 
but1 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but1))
but1.grid(row=1,column=1)
but2 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but2))
but2.grid(row=1,column=2)
but3 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but3))
but3.grid(row=2,column=0)
but4 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but4))
but4.grid(row=2,column=1)
but5 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but5))
but5.grid(row=2,column=2)
but6 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but6))
but6.grid(row=3,column=0)
but7 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but7))
but7.grid(row=3,column=1)
but8 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(but8))
but8.grid(row=3,column=2)
buttonRes = tkinter.Button (top, text='Restart',command=Restart)
buttonRes.grid(row=4,column=0)  
buttonQu = tkinter.Button (top, text='Quite',command=top.destroy)
buttonQu.grid(row=4,column=1)  


top.mainloop()


 