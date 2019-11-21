import tkinter
from tkinter import messagebox



top = tkinter.Tk()
top.title("Tic Tac Toc")
<<<<<<< HEAD

player1 = True
def place_marker(button):
        global player1 
        if button["text"]=="" and  player1==True:
            marker="X"
            button.configure(text=marker)
            if win_check(marker):
               messagebox.showinfo("Win", " X win ")
               play_agin()
            player1=False
        elif button["text"]=="" and player1==False:
            marker="O" 
            button.configure(text=marker)
            if win_check(marker):
               messagebox.showinfo("Win", " O win  ")
               play_agin()
            player1=True

def play_agin():
     message = messagebox.askquestion("Play agin","are you want to play agin?")
     if message == "yes":
        but0["text"]= but1["text"]= but2["text"]= but3["text"]= but4["text"]= but5["text"]= but6["text"]= but7["text"]= but8["text"]=""
     else :
         top.destroy()

def win_check(mark):
     return ((but6["text"] == mark and but7["text"] == mark and but8["text"]== mark) or # across the top
    (but3["text"] == mark and but4["text"] == mark and  but5["text"] == mark) or # across the middle
    (but0["text"] == mark and but1["text"]  == mark and but2["text"] == mark) or # across the bottom
    (but6["text"] == mark and but3["text"] == mark and but0["text"]  == mark) or # down the middle
    (but7["text"] == mark and but4["text"] == mark and but1["text"] == mark) or # down the middle
    (but8["text"] == mark and but5["text"] == mark and but2["text"] == mark) or # down the right side
    (but6["text"] == mark and but4["text"] == mark and but2["text"] == mark) or # diagonal
    (but8["text"] == mark and but4["text"]== mark and  but0["text"]  == mark)) # diagonal


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
=======
# use to store marker
board= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def place_marker(position,button):
    global player1
    if button["text"]=="" and  player1==True:
        marker="X"
        if win_check(board,"X"):
            print("win")
        player1=False
    elif button["text"]=="" and player1==False:
        marker="O"
        if win_check(board,"O"):
            print("win")
        player1=True
    board[position] = marker 
    button.configure(text=marker)


def win_check(board, mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

    
   

# Buttons
but0 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(1,but0))
but0.grid(row=1,column=0) 
but1 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(2,but1))
but1.grid(row=1,column=1)
but2 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(3,but2))
but2.grid(row=1,column=2)
but3 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(4,but3))
but3.grid(row=2,column=0)
but4 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(5,but4))
but4.grid(row=2,column=1)
but5 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(6,but5))
but5.grid(row=2,column=2)
but6 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(7,but6))
but6.grid(row=3,column=0)
but7 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(8,but7))
but7.grid(row=3,column=1)
but8 = tkinter.Button(top,text="" , width=10, height=5, command=lambda:place_marker(9,but8))
>>>>>>> 9cdee9896830d58787e405630918b65f356ae101
but8.grid(row=3,column=2)



top.mainloop()


 