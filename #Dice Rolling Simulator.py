#Dice Rolling Simulator
import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Dice Rolling Simulator")

# Create a label to display the result
result_label = tk.Label(root, font=("Helvetica", 32))
result_label.pack()

# Function to roll the dice
def roll_dice():
    # Generate a random number between 1 and 6
    result = random.randint(1, 6)
    # Update the result label with the new result
    result_label["text"] = str(result)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll the dice!", command=roll_dice)
roll_button.pack()

# Run the main loop
root.mainloop()
