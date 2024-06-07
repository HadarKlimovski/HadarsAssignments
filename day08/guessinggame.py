import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome To Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 20)
        self.guesses_taken = 0
        
        self.label = tk.Label(root, text="I'm thinking of a number between 1 and 20.")
        self.label.pack()
        
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()
        
        self.guess_button = tk.Button(root, text="Take a Guess", command=self.check_guess)
        self.guess_button.pack()
        
        self.show_button = tk.Button(root, text="Show Number", command=self.show_number)
        self.show_button.pack()
        
        self.restart_button = tk.Button(root, text="Restart Game", command=self.restart_game)
        self.restart_button.pack()
        
        self.exit_button = tk.Button(root, text="Exit Game", command=root.quit)
        self.exit_button.pack()
        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.guesses_taken += 1
            if guess < self.number_to_guess:
                self.result_label.config(text="Too low, try again!")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high, try again!")
            else:
                self.result_label.config(text=f"Good job! You guessed my number in {self.guesses_taken} guesses!")
                messagebox.showinfo("Congratulations", f"You guessed the number in {self.guesses_taken} guesses!")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def show_number(self):
        messagebox.showinfo("The Number", f"The number is {self.number_to_guess}.")

    def restart_game(self):
        self.number_to_guess = random.randint(1, 20)
        self.guesses_taken = 0
        self.guess_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.label.config(text="I'm thinking of a number between 1 and 20.")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
