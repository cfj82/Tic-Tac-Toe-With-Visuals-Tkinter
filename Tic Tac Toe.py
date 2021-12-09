# Tic Tac Toe with GUI

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.configure(width=300, height=250)

count = 0

def b1():
    global count
    if b1["text"] == "":
        b1["text"] = change()
        count = count + 1
        check()

def b2():
    global count
    if b2["text"] == "":
        b2["text"] = change()
        count = count + 1
        check()

def b3():
    global count
    if b3["text"] == "":
        b3["text"] = change()
        count = count + 1
        check()

def b4():
    global count
    if b4["text"] == "":
        b4["text"] = change()
        count = count + 1
        check()

def b5():
    global count
    if b5["text"] == "":
        b5["text"] = change()
        count = count + 1
        check()

def b6():
    global count
    if b6["text"] == "":
        b6["text"] = change()
        count = count + 1
        check()

def b7():
    global count
    if b7["text"] == "":
        b7["text"] = change()
        count = count + 1
        check()

def b8():
    global count
    if b8["text"] == "":
        b8["text"] = change()
        count = count + 1
        check()

def b9():
    global count
    if b9["text"] == "":
        b9["text"] = change()
        count = count + 1
        check()

def change():
    global count
    if count % 2 == 1:  # odd turn, player 1 is X
        output.set("Player 1 Turn")
        return "X"
    else:  # even turn
        output.set("Player 2 Turn")
        return "O"

def quit():
    msg = messagebox.askyesno("Quit", "Do You Want To Quit?")
    if msg == True:
        root.destroy()


def check():
    global count
    if (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or  # win top row
        b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or  # win middle row
        b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or  # win bottom row
        b7["text"] == "X" and b4["text"] == "X" and b1["text"] == "X" or  # win left column
        b8["text"] == "X" and b5["text"] == "X" and b2["text"] == "X" or  # win middle column
        b9["text"] == "X" and b6["text"] == "X" and b3["text"] == "X" or  # win right column
        b7["text"] == "X" and b5["text"] == "X" and b3["text"] == "X" or  # win diagonal
        b9["text"] == "X" and b5["text"] == "X" and b1["text"] == "X"):  # win other diagonal
        output.set("Player 1 Win!")
        quit()

    elif (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or  #win top row
        b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or  # win middle row
        b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or  # win bottom row
        b7["text"] == "O" and b4["text"] == "O" and b1["text"] == "O" or  # win left column
        b8["text"] == "O" and b5["text"] == "O" and b2["text"] == "O" or  # win middle column
        b9["text"] == "O" and b6["text"] == "O" and b3["text"] == "O" or  # win right column
        b7["text"] == "O" and b5["text"] == "O" and b3["text"] == "O" or  # win diagonal
        b9["text"] == "O" and b5["text"] == "O" and b1["text"] == "O"):  # win other diagonal
        output.set("Player 2 Win!")
        quit()


f_board = Frame(root, bg="#000000", borderwidth=2, )
f_board.rowconfigure([0,1,2,3], minsize=100)  # minsize for each row=100 keys
f_board.columnconfigure([0,1,2], minsize=100)
f_board.pack(fill="both", expand=True)

output = StringVar()
lbl = Label(f_board,  font=("verdana", 18), anchor="center", relief=SUNKEN, border=15,
                 bg="#5DADE2", textvariable=output)
lbl.grid(row=0, column=0, columnspan=2, sticky="nsew")

quit_btn = Button(f_board, font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 bg="#5DADE2", text="Quit", command=quit )
quit_btn.grid(row=0, column=2, sticky="nsew")

b7 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b7)
b7.grid(row=1, column=0, sticky="nsew")

b8 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b8)
b8.grid(row=1, column=1, sticky="nsew")

b9 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b9)
b9.grid(row=1, column=2, sticky="nsew")

b4 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b4)
b4.grid(row=2, column=0, sticky="nsew")

b5 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b5)
b5.grid(row=2, column=1, sticky="nsew")

b6 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b6)
b6.grid(row=2, column=2, sticky="nsew")

b1 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b1)
b1.grid(row=3, column=0, sticky="nsew")

b2 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b2)
b2.grid(row=3, column=1, sticky="nsew")

b3 = Button(f_board, text="", font=("verdana", 18), anchor="center", relief=RAISED, border=10,
                 activebackground="#A2D9CE", bg="#BB8FCE", command=b3)
b3.grid(row=3, column=2, sticky="nsew")

root.mainloop()