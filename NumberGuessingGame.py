from art import logo
from random import randint

EASY_LEVEL_ATTEMPTS = 10
MEDIUM_LEVEL_ATTEMPTS = 7
HARD_LEVEL_ATTEMPTS = 5
result_num = randint(1, 101)

def set_difficulty():

    level = input("Choose a difficulty level.Type 'easy', 'medium' or 'hard': ").lower()

    if level == "hard":
        attempts = HARD_LEVEL_ATTEMPTS
        return attempts

    elif level == "medium":
        attempts = MEDIUM_LEVEL_ATTEMPTS

    elif level == "easy":
        attempts = EASY_LEVEL_ATTEMPTS
        return attempts

    return None


def guess_number(attempts, result_number):
    while attempts > 0:

        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

            if user_guess > result_number:
                print("Too high.")
            elif user_guess < result_number:
                print("Too low.")
            elif user_guess == result_number:
                print(f"\nYou got it. The number is {result_number}!")
                break
            else:
                print("Please enter a valid input.")
                print("Guess again.")

            attempts -= 1

    else:
        print("You've run out of attempts to guesses, you lose.")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    attempts = set_difficulty()
    guess_number(attempts, result_num)


play_game()
while input("Do you want to play again? (y/n): ").lower() == "y":
    print("\n"*10)
    play_game()






