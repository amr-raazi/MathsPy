number = 1
while True:
  sum_factors = 0
  for possible_factor in range(1,number):
    if number % possible_factor == 0:
      sum_factors = sum_factors + possible_factor
  if sum_factors == number:
    print(str(number) + " is perfect")
  number += 1
 