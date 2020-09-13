import random
number_of_guesses = 1
max_guesses = 3
min_num_enter = 1
max_num_enter = 15
number = random.randint(min_num_enter, max_num_enter)
while True:
  guess = int(input(f'INPUT YOUR GUESS BETWEEN {min_num_enter} and {max_num_enter}'))
  if number_of_guesses > max_guesses:
    print(f'YOU LOST. THE CORRECT NUMBER WAS {number}')
    break
  elif int(guess) > max_num_enter or int(guess) < min_num_enter:
      print('PLEASE ENTER A VALID NUMBER')
  elif guess == number:
    print(f'YOU WON. YOU TOOK {number_of_guesses} guesses to guess {number}')
    break
  elif guess > number:
    number_of_guesses = number_of_guesses + 1
    print('TOO LARGE')

  elif guess < number:
    number_of_guesses = number_of_guesses + 1
    print('TOO SMALL')
