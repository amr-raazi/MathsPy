from tkinter import *
from tkinter import font as tkfont

# program variables
tic_tac_toe = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 1
winner = 0

# tkinter variables
root = Tk()
root.title("Tic Tac toe")
button_font = tkfont.Font(family="Times", size="24", weight="bold", slant="italic")

# top row
top_one = Button(root, text="", command=lambda: click_button(0, 0), width=7, height=2, font=button_font)
top_two = Button(root, text="", command=lambda: click_button(0, 1), width=7, height=2, font=button_font)
top_three = Button(root, text="", command=lambda: click_button(0, 2), width=7, height=2, font=button_font)

# middle row
middle_one = Button(root, text="", command=lambda: click_button(1, 0), width=7, height=2, font=button_font)
middle_two = Button(root, text="", command=lambda: click_button(1, 1), width=7, height=2, font=button_font)
middle_three = Button(root, text="", command=lambda: click_button(1, 2), width=7, height=2, font=button_font)

# bottom row
bottom_one = Button(root, text="", command=lambda: click_button(2, 0), width=7, height=2, font=button_font)
bottom_two = Button(root, text="", command=lambda: click_button(2, 1), width=7, height=2, font=button_font)
bottom_three = Button(root, text="", command=lambda: click_button(2, 2), width=7, height=2, font=button_font)

# button order
button_order = [[top_one, top_two, top_three], [middle_one, middle_two, middle_three],
                [bottom_one, bottom_two, bottom_three]]


# click button
def click_button(x, y):
    global turn
    # check if it is taken
    if tic_tac_toe[x][y] != 0:
        return
    # set in matrix
    tic_tac_toe[x][y] = turn
    # set button text and change turn
    if turn == 1:
        button_order[x][y]["text"] = "X"
        turn = 2
    else:
        button_order[x][y]["text"] = "O"
        turn = 1
    # check win conditions
    evaluate()


# eveluate win conditions
def evaluate():
    global tic_tac_toe, winner
  #  print(tic_tac_toe[1][1])
    # horizontal check
    for line in tic_tac_toe:
        if line.count(1) == 3 or line.count(2) == 3:
            winner = line[0]
    # vertical check
    for x in range(3):
        if tic_tac_toe[0][x] == tic_tac_toe[1][x] == tic_tac_toe[2][x]:
            winner = tic_tac_toe[0][x]
    # diagonal checking
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] or tic_tac_toe[0][2] == tic_tac_toe[1][1] == \
            tic_tac_toe[2][0]:
        winner = tic_tac_toe[1][1]
        print(winner)
    # check if a player won
    if winner != 0:
        winning_sequence()


# win sequence
def winning_sequence():
    global winner, root
    if winner == 1:
        winner = "X"
    else:
        winner = "O"
    root.destroy()
    root = Tk()
    Label(text=f"Player who was playing symbol {winner} won!", font=button_font).pack()
    Button(text=f"Exit", command=lambda: root.destroy(), font=button_font).pack()
    root.mainloop()


# pack in grid
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
