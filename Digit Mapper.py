numbers = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six",
           "7": "Seven", "8": "Eight", "9": "Nine", "0": "Zero"}
count = 0
inp = input("Input Number")
output = ""
while count < len(inp):
    number = inp[count]
    output += str(numbers.get(number, "NA")) + " "
    count += 1
print(output)
