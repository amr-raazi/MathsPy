from time import sleep

from sympy import tan, isprime

initialnum = 1169809367327212570704813632106852886389036911
num = initialnum + 1
limit = 1000000
count = 1
delay = 0.2
while True:
    strnum = str(num)
    tannum = tan(num)
    if tannum > num and isprime(num) == True:
        print(strnum + " is prime and it's tan is greater than it. " + str(
            count - 1) + " numbers were checked to find this number")
        break
    elif num == limit:
        break
    else:
        if count == 1:
            if isprime(num) == False and tan(num) < num:
                print(strnum + " is neither prime nor is it's tan greater than it. " + str(
                    count) + " number has been checked")
            elif isprime(num) == True and tan(num) < num:
                print(strnum + " is prime but it's tan is less than it. " + str(count) + " number has been checked")
            elif isprime(num) == False and tan(num) > num:
                print(strnum + " is not prime but it's tan is greater than it. " + str(
                    count) + " number has been checked")
        elif count > 1:
            if isprime(num) == False and tan(num) < num:
                print(strnum + " is neither prime nor is it's tan greater than it. " + str(
                    count) + " numbers have been checked")
            elif isprime(num) == True and tan(num) < num:
                print(strnum + " is prime but it's tan is less than it. " + str(count) + " numbers have been checked")
            elif isprime(num) == False and tan(num) > num:
                print(strnum + " is not prime but it's tan is greater than it. " + str(
                    count) + " numbers have been checked")
        num += 1
    count += 1
    sleep(delay)
