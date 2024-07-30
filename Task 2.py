import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare the guess to the generated number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    guessing_game()
