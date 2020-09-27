from tkinter import *
from tkinter import font as tkfont

# program variables
tic_tac_toe = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
turn = 1
winner = 0

# tkinter variables
root = Tk()
root.title("Tic Tac toe 5x5")
button_font = tkfont.Font(family="Times", size="24", weight="bold", slant="italic")

# first row
first_one = Button(root, text="", command=lambda: click_button(0, 0), width=7, height=2, font=button_font)
first_two = Button(root, text="", command=lambda: click_button(0, 1), width=7, height=2, font=button_font)
first_three = Button(root, text="", command=lambda: click_button(0, 2), width=7, height=2, font=button_font)
first_four = Button(root, text="", command=lambda: click_button(0, 3), width=7, height=2, font=button_font)
first_five = Button(root, text="", command=lambda: click_button(0, 4), width=7, height=2, font=button_font)

# second row
second_one = Button(root, text="", command=lambda: click_button(1, 0), width=7, height=2, font=button_font)
second_two = Button(root, text="", command=lambda: click_button(1, 1), width=7, height=2, font=button_font)
second_three = Button(root, text="", command=lambda: click_button(1, 2), width=7, height=2, font=button_font)
second_four = Button(root, text="", command=lambda: click_button(1, 3), width=7, height=2, font=button_font)
second_five = Button(root, text="", command=lambda: click_button(1, 4), width=7, height=2, font=button_font)

# third row
third_one = Button(root, text="", command=lambda: click_button(2, 0), width=7, height=2, font=button_font)
third_two = Button(root, text="", command=lambda: click_button(2, 1), width=7, height=2, font=button_font)
third_three = Button(root, text="", command=lambda: click_button(2, 2), width=7, height=2, font=button_font)
third_four = Button(root, text="", command=lambda: click_button(2, 3), width=7, height=2, font=button_font)
third_five = Button(root, text="", command=lambda: click_button(2, 4), width=7, height=2, font=button_font)

# fourth row
fourth_one = Button(root, text="", command=lambda: click_button(3, 0), width=7, height=2, font=button_font)
fourth_two = Button(root, text="", command=lambda: click_button(3, 1), width=7, height=2, font=button_font)
fourth_three = Button(root, text="", command=lambda: click_button(3, 2), width=7, height=2, font=button_font)
fourth_four = Button(root, text="", command=lambda: click_button(3, 3), width=7, height=2, font=button_font)
fourth_five = Button(root, text="", command=lambda: click_button(3, 4), width=7, height=2, font=button_font)

# fifth row
fifth_one = Button(root, text="", command=lambda: click_button(4, 0), width=7, height=2, font=button_font)
fifth_two = Button(root, text="", command=lambda: click_button(4, 1), width=7, height=2, font=button_font)
fifth_three = Button(root, text="", command=lambda: click_button(4, 2), width=7, height=2, font=button_font)
fifth_four = Button(root, text="", command=lambda: click_button(4, 3), width=7, height=2, font=button_font)
fifth_five = Button(root, text="", command=lambda: click_button(4, 4), width=7, height=2, font=button_font)

# button order
button_order = [[first_one, first_two, first_three, first_four, first_five], [second_one, second_two, second_three, second_four, second_five],
                [third_one, third_two, third_three, third_four, third_five], [fourth_one, fourth_two, fourth_three, fourth_four, fourth_five],
                [fifth_one, fifth_two, fifth_three, fifth_four, fifth_five]]


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


# evaluate win conditions
def evaluate():
    global tic_tac_toe, winner
    # horizontal check
    for line in tic_tac_toe:
        if line.count(1) == 5 or line.count(2) == 5:
            winner = line[0]
    # vertical check
    for x in range(5):
        if tic_tac_toe[0][x] == tic_tac_toe[1][x] == tic_tac_toe[2][x] == tic_tac_toe[3][x] == tic_tac_toe[4][x]:
            if tic_tac_toe[0][x] != 0:
                winner = tic_tac_toe[0][x]
    # diagonal checking
    if tic_tac_toe[0][0] == tic_tac_toe[1][1] == tic_tac_toe[2][2] == tic_tac_toe[3][3] == tic_tac_toe[4][4] or \
            tic_tac_toe[0][-1] == tic_tac_toe[1][-2] == tic_tac_toe[2][-3] == tic_tac_toe[3][-4] == tic_tac_toe[4][-5]:
        winner = tic_tac_toe[2][2]
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
first_one.grid(row=0, column=0)
first_two.grid(row=0, column=1)
first_three.grid(row=0, column=2)
first_four.grid(row=0, column=3)
first_five.grid(row=0, column=4)

second_one.grid(row=1, column=0)
second_two.grid(row=1, column=1)
second_three.grid(row=1, column=2)
second_four.grid(row=1, column=3)
second_five.grid(row=1, column=4)

third_one.grid(row=2, column=0)
third_two.grid(row=2, column=1)
third_three.grid(row=2, column=2)
third_four.grid(row=2, column=3)
third_five.grid(row=2, column=4)

fourth_one.grid(row=3, column=0)
fourth_two.grid(row=3, column=1)
fourth_three.grid(row=3, column=2)
fourth_four.grid(row=3, column=3)
fourth_five.grid(row=3, column=4)

fifth_one.grid(row=4, column=0)
fifth_two.grid(row=4, column=1)
fifth_three.grid(row=4, column=2)
fifth_four.grid(row=4, column=3)
fifth_five.grid(row=4, column=4)

root.mainloop()
