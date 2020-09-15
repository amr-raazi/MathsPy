from tkinter import *
from tkinter import font as tkfont
import math

# program variable
operator_number = []

# initiating instance
root = Tk()

# title
root.title("Calculator")

# define font
button_font = tkfont.Font(family="Times", size="24", weight="bold", slant="italic")
equal_button_font = tkfont.Font(family="Times", size="20", weight="bold", slant="italic")
clear_button_font = tkfont.Font(family="Courier", size="24", weight="bold", slant="italic")
backspace_font = tkfont.Font(family="Courier", size="24", weight="bold", slant="italic")
box_font = tkfont.Font(family="Helvetica", size="26", weight="bold", slant="roman")
Button.borderwidth = 10

# create entry box
box = Entry(root, font=box_font, width=28, )
box.grid(row=0, column=0, columnspan=4, pady=20)
box.configure(state="disabled")


# number button command
def number_button(num):
    current_num = box.get()
    current_num += str(num)
    box.configure(state="normal")
    box.delete(0, END)
    box.insert(0, current_num)
    box.configure(state="disabled")
    return current_num


# clear button command
def clear_button():
    box.configure(state="normal")
    box.delete(0, END)
    box.configure(state="disabled")
    return None


# operator button command
def operator_button(operator):
    global operator_number
    first_number = box.get()
    operator_number = [operator, first_number]
    box.configure(state="normal")
    box.delete(0, END)
    box.configure(state="disabled")
    return operator_number


# decimal button command
def decimal_button():
    list_of_numbers = list(box.get())
    if "." not in list_of_numbers:
        current_num = box.get()
        current_num += "."
        box.configure(state="normal")
        box.delete(0, END)
        box.insert(0, current_num)
        box.configure(state="disabled")
    else:
        print("Decimal already added")
    return None


# backspace button command
def backspace_button():
    list_of = list(box.get())
    list_of.pop()
    str1 = ''.join(str(e) for e in list_of)
    box.insert(0, str1)


# equal button command
def equal_button():
    global operator_number
    try:
        second_number = float(box.get())
        first_number = float(operator_number[1])
        operator = operator_number[0]
        if operator == "/":
            number = first_number / second_number
        elif operator == "*":
            number = first_number * second_number
        elif operator == "-":
            number = first_number - second_number
        elif operator == "+":
            number = first_number + second_number
        else:
            number = second_number
        if math.ceil(number) == number:
            number = int(number)
    except (IndexError, ValueError):
        if len(operator_number) == 0:
            if not len(box.get()) == 0:
                number = box.get()
            else:
                number = 0
        else:
            number = operator_number[1]
    box.configure(state="normal")
    box.delete(0, END)
    box.insert(0, number)
    box.configure(state="disabled")


# number buttons
one_button = Button(root, text="1", command=lambda: number_button(1), width=7, height=2, font=button_font)
two_button = Button(root, text="2", command=lambda: number_button(2), width=7, height=2, font=button_font)
three_button = Button(root, text="3", command=lambda: number_button(3), width=7, height=2, font=button_font)
four_button = Button(root, text="4", command=lambda: number_button(4), width=7, height=2, font=button_font)
five_button = Button(root, text="5", command=lambda: number_button(5), width=7, height=2, font=button_font)
six_button = Button(root, text="6", command=lambda: number_button(6), width=7, height=2, font=button_font)
seven_button = Button(root, text="7", command=lambda: number_button(7), width=7, height=2, font=button_font)
eight_button = Button(root, text="8", command=lambda: number_button(8), width=7, height=2, font=button_font)
nine_button = Button(root, text="9", command=lambda: number_button(9), width=7, height=2, font=button_font)
zero_button = Button(root, text="0", command=lambda: number_button(0), width=7, height=2, font=button_font)

# operator buttons
add_button = Button(root, text="+", command=lambda: operator_button("+"), width=7, height=2, font=button_font)
subtract_button = Button(root, text="-", command=lambda: operator_button("-"), width=7, height=2,
                         font=button_font)
multiply_button = Button(root, text="×", command=lambda: operator_button("*"), width=7, height=2,
                         font=button_font)
division_button = Button(root, text="÷", command=lambda: operator_button("/"), width=7, height=2,
                         font=button_font)

# misc
decimal_button = Button(root, text=".", command=decimal_button, width=7, height=2, font=button_font)
equal_button = Button(root, text="=", command=equal_button, width=8, height=6, font=equal_button_font)
clear_button = Button(root, text="clear", command=clear_button, width=14, height=2, font=clear_button_font)
backspace_button = Button(root, text="back", command=backspace_button, width=7, height=2, font=backspace_font)

# fit into grid
one_button.grid(row=1, column=0)
two_button.grid(row=1, column=1)
three_button.grid(row=1, column=2)
four_button.grid(row=2, column=0)
five_button.grid(row=2, column=1)
six_button.grid(row=2, column=2)
seven_button.grid(row=3, column=0)
eight_button.grid(row=3, column=1)
nine_button.grid(row=3, column=2)
zero_button.grid(row=3, column=3)

add_button.grid(row=4, column=0, columnspan=1)
subtract_button.grid(row=4, column=1, columnspan=1)
multiply_button.grid(row=4, column=2, columnspan=1)
division_button.grid(row=4, column=3, columnspan=1)

equal_button.grid(row=1, column=3, rowspan=2)
decimal_button.grid(row=5, column=0)
backspace_button.grid(row=5, column=3)
clear_button.grid(row=5, column=1, columnspan=2)

# mainloop
root.mainloop()
