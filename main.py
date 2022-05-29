# Number Guessing Game
# Need to add a life counter to the game

import random  # will be used to generate the random numbers


def number_generator():
    print("Hello Welcome to the number guessing game,"
          "Hope u Enjoy :)"
          )
    # To take users input on desired number range
    number_range1 = int(input("Enter 1st range number: \t"))
    number_range2 = int(input("Enter 2nd range number \t"))
    # Generating the number based on user input
    generated_number = random.randint(number_range1, number_range2)
    print(f"You have selected number range {number_range1} - {number_range2}")
    # Capturing users input on guessed Number
    answer = int(input("Enter First Guess: "))
    # while loop to check if the user input == to the generated number
    while answer != generated_number:
        print("Naaa That ain't it try again")
        answer = int(input("Enter First Guess: "))
        if answer == generated_number:
            break
    print(f"Yaaay u won the number is {generated_number}")


if __name__ == '__main__':
    number_generator()
