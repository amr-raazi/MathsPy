import math
import sys


def is_prime(number):
    try:
        prime = True
        if number < 0:
            return False
        elif number in (2, 3):
            return True
        elif number in (0, 1, 4):
            return False
        else:
            for potential_factor in range(2, math.ceil(number / 2)):
                if not number % potential_factor:
                    prime = False
            if prime:
                return True
            else:
                return False
    except TypeError or ValueError:
        return "Please enter a valid integer"


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))
