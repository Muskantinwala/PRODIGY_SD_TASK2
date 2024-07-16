import random

def main():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("I have generated a random number between 1 and 100.")
    print("Try to guess it!")

    while not guessed_correctly:
        # Prompt the user to input their guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare the guess to the generated number and provide feedback
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    main()
