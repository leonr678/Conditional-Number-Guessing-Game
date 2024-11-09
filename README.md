# Conditional-Number-Guessing-Game
This is a Conditional Number guessing game, using Python. The game has a simple GUI and requires no external libraries.

# How to play

When the game is run, you will be able to choose a difficulty which essentially chooses a specific range of numbers for you: easy (1-30), medium (1-50), hard (1-100).
Once a difficulty is chosen, a mathematical condition is provided for you so you know what type of number to guess, e.g., "Guess a number between 1 and 50, given the number is a multiple of 4".
You will have 5 attempts before Game Over.

# Libraries

All libraries are included with Python:

- ***TKinter (GUI)***
- ***Random***
- ***Math***  


# Programming

We make use of GUI, error handling, randomization, input validation, and conditional logic.
The game is contained in a class called ConditionalNumberGuessing, which contains many methods that control different aspects of the game, such as check_guess() which determines whether the user's guess matches the target number. Our game is event-driven, meaning the flow of execution is determined by the user input.
