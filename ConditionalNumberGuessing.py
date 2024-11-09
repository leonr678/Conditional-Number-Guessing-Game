# Welcome to Conditional Number Guessing!

# All modules are included with Python
import tkinter as tk
from tkinter import messagebox
import random
import math

# Lists required for setting conditions
easy_conditions = ["less than 10", "greater than 15", "an even number", "a multiple of 3", "a multiple of 4", "a multiple of 5", "multiple of 6", "greater than 20"]
medium_conditions = ["less than 18", "greater than 29", "an even number", "a multiple of 3", "a multiple of 4", "a multiple of 5", "multiple of 6", "greater than 38"]
hard_conditions = ["less than 29", "greater than 64", "an even number", "a multiple of 3", "a multiple of 4", "a multiple of 5", "multiple of 6", "greater than 77"]

class ConditionalNumberGuessing:  # The game is contained in this class
    def __init__(self, root):
        self.root = root
        self.root.title("Conditional Number Guessing!")
        self.target_num = 0
        self.max_num = 0
        self.guess_counter = 1
        self.easy_condition_counter = random.randint(0, len(easy_conditions) - 1)
        self.medium_condition_counter = random.randint(0, len(easy_conditions) - 1)
        self.hard_condition_counter = random.randint(0, len(easy_conditions) - 1)
        # UI for difficulty
        self.main_label = tk.Label(root, text="Choose your difficulty!", font=("CenturyGothic", 22))
        self.sub_label = tk.Label(root, text="The difficulty is chosen each round.", font=("Arial", 16, "bold italic"))
        self.guess_label = tk.Label(root, text=f"Guess: {self.guess_counter}/5", font=("CenturyGothic", 15))
        self.main_label.pack(pady=5)
        self.sub_label.pack(pady=5)
        self.easy_button = tk.Button(root, text="Easy", command=self.easy_game)
        self.easy_button.pack(pady=3)
        self.medium_button = tk.Button(root, text="Medium", command=self.medium_game)
        self.medium_button.pack(pady=3)
        self.hard_button = tk.Button(root, text="Hard", command=self.hard_game)
        self.hard_button.pack(pady=3)

    def easy_game(self):
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.guess_label.config(text=f"Guess: {self.guess_counter}/5")
        self.guess_label.pack()
        self.sub_label.config(text="")
        self.easy_condition_counter = (self.easy_condition_counter + 1) % len(easy_conditions)
        self.main_label.config(text="Guess a number between 1 and 30, given that the number is " + easy_conditions[self.easy_condition_counter])
        self.easy_number_picker(self.easy_condition_counter)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.guess_button = tk.Button(root, text="Confirm", command=self.check_guess)
        self.guess_button.pack(pady=2)
        self.max_num = 30

    def easy_number_picker(self, x):
        if x == 0:
            self.target_num = random.randint(1, 10)
        elif x == 1:
            self.target_num = random.randint(15, 30)    
        elif 1 < x < 7:
            self.target_num = random.randint(1, math.floor(30/x)) * x   # Multiple of x between 1 and 30
        elif x == 7:
            self.target_num = random.randint(20, 30)    

    def medium_game(self):
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.guess_label.pack()
        self.sub_label.config(text="")
        self.medium_condition_counter = (self.medium_condition_counter + 1) % len(medium_conditions)
        self.main_label.config(text="Guess a number between 1 and 50, given that the number is " + medium_conditions[self.medium_condition_counter])
        self.medium_number_picker(self.medium_condition_counter)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.guess_button = tk.Button(root, text="Confirm", command=self.check_guess)
        self.guess_button.pack(pady=2)
        self.max_num = 50

    def medium_number_picker(self, x):
        if x == 0:
            self.target_num = random.randint(1, 18)
        elif x == 1:
            self.target_num = random.randint(29, 50)    
        elif 1 < x < 7:
            self.target_num = random.randint(1, math.floor(50/x)) * x   # Multiple of x between 1 and 50
        elif x == 7:
            self.target_num = random.randint(38, 50)    

    def hard_game(self):
        self.easy_button.pack_forget()
        self.medium_button.pack_forget()
        self.hard_button.pack_forget()
        self.guess_label.pack()
        self.sub_label.config(text="")
        self.hard_condition_counter = (self.hard_condition_counter + 1) % len(hard_conditions)
        self.main_label.config(text="Guess a number between 1 and 100, given that the number is " + hard_conditions[self.hard_condition_counter])
        self.hard_number_picker(self.hard_condition_counter)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        self.guess_button = tk.Button(root, text="Confirm", command=self.check_guess)
        self.guess_button.pack(pady=2)
        self.max_num = 100

    def hard_number_picker(self, x):
        if x == 0:
            self.target_num = random.randint(1, 29)
        elif x == 1:
            self.target_num = random.randint(64, 100)    
        elif 1 < x < 7:
            self.target_num = random.randint(1, math.floor(100/x)) * x   # Multiple of x between 1 and 100
        elif x == 7:
            self.target_num = random.randint(77, 100)    



    def check_guess(self):  # Determines if the guessed number was correct
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > self.max_num:
                self.sub_label.config(text="Number is not in range, try again!")
                self.entry.delete(0, tk.END)
                if self.guess_counter == 5:
                    messagebox.showinfo(title="Tough luck!", message=f"Ran out of guesses!!! The number was {self.target_num}.")
                    self.reset_game()
            elif guess != self.target_num:
                self.sub_label.config(text="Incorrect, try again!")
                self.entry.delete(0, tk.END)
                if self.guess_counter == 5:
                    messagebox.showinfo(title="Tough luck!",message=f"Ran out of guesses!!! The number was {self.target_num}.")
                    self.reset_game()
            else:
                if self.guess_counter > 1:
                    messagebox.showinfo(title="Congratulations!",message=f"You guessed the right number!!! It took you {self.guess_counter} attempts.")
                else:
                    messagebox.showinfo(title="Congratulations!",message=f"You guessed the right number!!! It took you {self.guess_counter} attempt.")
                self.entry.delete(0, tk.END)
                self.reset_game()
            self.guess_counter += 1
            self.guess_label.config(text=f"Guess: {self.guess_counter}/5")
            #self.guess_label.pack()    
        except ValueError:
                self.sub_label.config(text="Not a valid number")
                

    def reset_game(self): # Reset the game back to it's original state
        self.main_label.config(text="Choose your difficulty")
        self.sub_label.config(text="The difficulty is chosen each round.")
        self.guess_counter = 0
        self.guess_label.pack_forget()
        self.guess_button.pack_forget()
        self.easy_button.pack(pady=3)
        self.medium_button.pack(pady=3)
        self.hard_button.pack(pady=3)
        self.entry.pack_forget()


# main
root = tk.Tk()  # Create window
root.geometry("900x300")  # Size of window
game = ConditionalNumberGuessing(root)  # Create an instance of the class
root.mainloop()                              

                              
