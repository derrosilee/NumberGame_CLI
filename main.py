# Number Guessing Game

import random  # will be used to generate the random numbers


def index():  # will add function
    number_range1 = int(input("Enter 1st range number: \t"))
    number_range2 = int(input("Enter 2nd range number \t"))
    generated_number = random.randint(number_range1, number_range2)
    print(f"The Generated Number is {generated_number}")


if __name__ == '__main__':
    index()
