import tkinter as tk
from tkinter import messagebox
import random

# create window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")

# generate random number
number = random.randint(1, 100)

# function to check guess
def check_guess():
    try:
        guess = int(entry.get())

        if guess < number:
            messagebox.showinfo("Result", "Too Low! Try again.")
        elif guess > number:
            messagebox.showinfo("Result", "Too High! Try again.")
        else:
            messagebox.showinfo("Congratulations 🎉", "You guessed it right!")
            root.destroy()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# UI elements
label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Check Guess", command=check_guess, font=("Arial", 11))
button.pack(pady=10)

root.mainloop()
