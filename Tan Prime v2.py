from sympy import tan
from sympy.ntheory import isprime

num = 1169809367327212570704813632106852886389036911 + 1
while True:
    strnum = str(num)
    tannum = tan(num)
    if num % 100000 == 0:
        print(strnum + " has been checked")
        num += 1
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0 or num % 13 == 0 or num % 17 == 0 or num % 23 == 0 or num % 29 == 0 or num % 31 == 0 or num % 37 == 0 or num % 41 == 0 or num % 43 == 0 or num % 47 == 0 or num % 53 == 0 or num % 59 == 0 or num % 61 == 0 or num % 67 == 0 or num % 71 == 0 or num % 73 == 0 or num % 79 == 0 or num % 83 == 0 or num % 89 == 0 or num % 97 == 0:
        num += 1
    elif isprime(num) and tannum > num:
        print(strnum + " is prime and it's tan is greater than it.")
        break
    else:
        num += 1
