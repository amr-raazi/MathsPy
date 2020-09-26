from tkinter import *
from tkinter import font as tkfont

tic_tac_toe = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
root = Tk()
root.title("Tic Tac toe")
button_font = tkfont.Font(family="Times", size="24", weight="bold", slant="italic")
turn = 1
winner = 0

top_one = Button(root, text="", command=lambda: click_button(0, 0), width=7, height=2, font=button_font)
top_two = Button(root, text="", command=lambda: click_button(0, 1), width=7, height=2, font=button_font)
top_three = Button(root, text="", command=lambda: click_button(0, 2), width=7, height=2, font=button_font)

middle_one = Button(root, text="", command=lambda: click_button(1, 0), width=7, height=2, font=button_font)
middle_two = Button(root, text="", command=lambda: click_button(1, 1), width=7, height=2, font=button_font)
middle_three = Button(root, text="", command=lambda: click_button(1, 2), width=7, height=2, font=button_font)

bottom_one = Button(root, text="", command=lambda: click_button(2, 0), width=7, height=2, font=button_font)
bottom_two = Button(root, text="", command=lambda: click_button(2, 1), width=7, height=2, font=button_font)
bottom_three = Button(root, text="", command=lambda: click_button(2, 2), width=7, height=2, font=button_font)

button_order = [[top_one, top_two, top_three], [middle_one, middle_two, middle_three],
                [bottom_one, bottom_two, bottom_three]]


def click_button(x, y):
    global turn
    if tic_tac_toe[x][y] != 0:
        return
    tic_tac_toe[x][y] = turn
    if turn == 1:
        button_order[x][y]["text"] = "X"
        turn = 2
    else:
        button_order[x][y]["text"] = "O"
        turn = 1
    evaluate()


def evaluate():
    global tic_tac_toe, winner, root
    # horizontal check
    for line in tic_tac_toe:
        if line.count(1) == 3 or line.count(2) == 3:
            winner = line[0]
    for x in range(3):
        if tic_tac_toe[0][x] == tic_tac_toe[1][x] == tic_tac_toe[2][x] == 1 or tic_tac_toe[0][x] \
                == tic_tac_toe[1][x] == tic_tac_toe[2][x] == 2:
            winner = tic_tac_toe[0][x]
    # diagonal checking
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] == 1 or tic_tac_toe[0][0] == tic_tac_toe[1][1] == \
            tic_tac_toe[2][2] == 2:
        winner = tic_tac_toe[1][1]
    if winner != 0:
        if winner == 1:
            winner = "X"
        else:
            winner = "O"
        root.destroy()
        root = Tk()
        Label(text=f"Player who was playing symbol {winner} won!", font=button_font).pack()
        Button(text=f"Exit", command=lambda: root.destroy(), font=button_font).pack()
        root.mainloop()


top_one.grid(row=1, column=0)
top_two.grid(row=1, column=1)
top_three.grid(row=1, column=2)
middle_one.grid(row=2, column=0)
middle_two.grid(row=2, column=1)
middle_three.grid(row=2, column=2)
bottom_one.grid(row=3, column=0)
bottom_two.grid(row=3, column=1)
bottom_three.grid(row=3, column=2)
root.mainloop()
