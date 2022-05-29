# Number Guessing Game

import random  # will be used to generate the random numbers


def number_generator():  # will add function
    # To take users input on desired number range
    number_range1 = int(input("Enter 1st range number: \t"))
    number_range2 = int(input("Enter 2nd range number \t"))
    # Generating the number based on user input
    generated_number = random.randint(number_range1, number_range2)
    print(f"You have selected number range {number_range1} - {number_range2}")
    # Capturing users input on guessed Number
    answer = int(input("Enter First Guess: "))
    # Condition Checking
    while answer != generated_number:
        print("Naaa That ain't it try again")
        answer = int(input("Enter First Guess: "))
        if answer == generated_number:
            break
    print(f"Congratulations u won the number is {generated_number}")


if __name__ == '__main__':
    number_generator()
