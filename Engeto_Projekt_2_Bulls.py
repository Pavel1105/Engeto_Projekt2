"""
projekt_2_bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Pavel Soukal
email: pavel.soukal@icloud.com
discord: paso_97533
"""
import random

def generate_secret_number():
    first_digit = random.choice('123456789')  # First digit: 1-9
    remaining_digits = random.sample('0123456789'.replace(first_digit, ''), 3)  # Sample without the first digit
    return first_digit + ''.join(remaining_digits)

# Test the function
print(generate_secret_number())


def validate_input(user_input, secret_number):
    if not user_input.isdigit() or len(user_input) != 4 or len(set(user_input)) != 4 or user_input[0] == '0':
        return False
    return True

def evaluate_guess(user_input, secret_number):
    bulls = sum(user_input[i] == secret_number[i] for i in range(4))
    cows = sum(user_input[i] in secret_number for i in range(4)) - bulls
    return bulls, cows

def bulls_and_cows_game():
    secret_number = generate_secret_number()
    attempts = 0

    print("Hi there!\n"
          "-----------------------------------------------\n"
          "I've generated a random 4 digit number for you.\n"
          "Let's play a bulls and cows game.\n"
          "-----------------------------------------------")

    while True:
        user_input = input("Enter a number: ")

        if not validate_input(user_input, secret_number):
            print("Invalid input. Please enter a 4-digit number with unique digits and no leading zeros.")
            continue

        bulls, cows = evaluate_guess(user_input, secret_number)
        attempts += 1

        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} {'guess' if attempts == 1 else 'guesses'}!")
            break

if __name__ == "__main__":
    bulls_and_cows_game()
