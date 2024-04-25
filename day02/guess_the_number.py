import random
print('Hello my friend! welcome to my guessing game!')
number_to_guess = random.randint(1, 20)
guesses_taken = 0
print("I'm thinking of a number between 1 and 20")

while True:
    guess = int(input("Take a guess: "))
    guesses_taken += 1

    if guess < number_to_guess:
        print("Too low, try again!")
    elif guess > number_to_guess:
        print("Too high, Try again!")
    else:
        print(f"Good job Friend! You guessed my number in {guesses_taken} guesses!")
        break
