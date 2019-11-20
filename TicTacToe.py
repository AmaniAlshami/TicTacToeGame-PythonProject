import tkinter

top = tkinter.Tk()
top.title("Tic Tac Toc")
# use to store marker
board= [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def place_marker(position,marker,button):
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
but0 = tkinter.Button(top,text="1" , width=10, height=5, command=lambda:place_marker(1,"X",but0))
but0.grid(row=1,column=0)
but1 = tkinter.Button(top,text="2" , width=10, height=5, command=lambda:place_marker(2,"O",but1))
but1.grid(row=1,column=1)
but2 = tkinter.Button(top,text="3" , width=10, height=5)
but2.grid(row=1,column=2)
but3 = tkinter.Button(top,text="4" , width=10, height=5)
but3.grid(row=2,column=0)
but4 = tkinter.Button(top,text="5" , width=10, height=5)
but4.grid(row=2,column=1)
but5 = tkinter.Button(top,text="6" , width=10, height=5)
but5.grid(row=2,column=2)
but6 = tkinter.Button(top,text="7" , width=10, height=5)
but6.grid(row=3,column=0)
but7 = tkinter.Button(top,text="8" , width=10, height=5)
but7.grid(row=3,column=1)
but8 = tkinter.Button(top,text="9" , width=10, height=5)
but8.grid(row=3,column=2)




top.mainloop()


 