e = "2.718281828459045235360287471352662497757247093699959574966"

for i, digit in enumerate(e):
    inputted_digit = input(f"Enter the {i} digit")
    if inputted_digit != digit:
        print(f"Wrong digit, you entered {inputted_digit} while correct digit was {digit}")
        break
