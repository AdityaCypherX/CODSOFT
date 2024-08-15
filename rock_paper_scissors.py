import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the computer's choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# Function to handle game logic and display results
def play(choice):
    global user_score, computer_score
    
    computer_choice = get_computer_choice()
    result = ""
    
    if choice == computer_choice:
        result = f"It's a tie! Both chose {choice}."
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! {choice} beats {computer_choice}."
        user_score += 1
    else:
        result = f"You lose! {computer_choice} beats {choice}."
        computer_score += 1
    
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def play_again():
    result_label.config(text="")
    choice_var.set("")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create and place widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Rock", width=10, height=2, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, height=2, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, height=2, command=lambda: play("Scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14))
score_label.pack(pady=10)

tk.Button(root, text="Play Again", width=10, height=2, command=play_again).pack(pady=10)

# Variable to store user choice
choice_var = tk.StringVar()

# Run the application
root.mainloop()
