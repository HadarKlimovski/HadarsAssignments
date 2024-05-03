import random

def main():
    print("Hello, welcome to my guessing game!")

    while True:
        number_to_guess = random.randint(1, 20)
        guesses_taken = 0
        print("I'm thinking of a number between 1 and 20.")

        while True:
            guess = input("Take a guess (or 's' to show the number): ")
            if guess.lower() == "s":
                print(f"The number is {number_to_guess}.")
                continue

            try:
                guess = int(guess)
                guesses_taken += 1
                if guess < number_to_guess:
                    print("Too low, try again!")
                elif guess > number_to_guess:
                    print("Too high, try again!")
                else:
                    print(f"Good job! You guessed my number in {guesses_taken} guesses!")
                    break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            decision = input("Type 'x' to exit, 'n' to start a new game: ").lower()
            if decision == "x":
                print("Thank you for playing with me! Goodbye!")
                exit()
            elif decision == "n":
                break
            else:
                print("Invalid command. Please choose 'x' or 'n'.")

        if decision == "n":
            continue

if __name__ == "__main__":
    main()

