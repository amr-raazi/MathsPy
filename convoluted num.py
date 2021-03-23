import random


def convoluted_num(target):
    operators = ["+", "-", "*"]
    sequence = "100"
    for _ in range(random.randint(600, 700)):
        number = random.randint(1, 100)
        sequence += f"{random.choice(operators)}{number}"
    res = eval(sequence)
    if res > target:
        sequence += f"-{res - target}"
    if res < target:
        sequence += f"+{target - res}"
    if len(sequence) < 2000:
        return sequence
    print("recursion")
    return convoluted_num(target)


print(convoluted_num(36))
