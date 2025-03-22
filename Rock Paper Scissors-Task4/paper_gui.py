import tkinter as tk
from tkinter import messagebox
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]

# Score tracking
user_score = 0
computer_score = 0

# Function to determine the winner
def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie! 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 💻🏆"
        computer_score += 1

    # Update the display
    result_label.config(text=f"You: {user_choice} \nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    # Show Play Again button
    play_again_button.pack(pady=10)

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0  # Reset user score
    computer_score = 0  # Reset computer score

    result_label.config(text="Choose your move!")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    play_again_button.pack_forget()  # Hide Play Again button

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Choose your move!", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock 🪨", font=("Arial", 12), command=lambda: play_game("Rock"), width=10).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper 📄", font=("Arial", 12), command=lambda: play_game("Paper"), width=10).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors ✂️", font=("Arial", 12), command=lambda: play_game("Scissors"), width=11).grid(row=0, column=2, padx=10)

# Play Again Button (Initially Hidden)
play_again_button = tk.Button(root, text="Play Again 🔄", font=("Arial", 12), command=reset_game, bg="#FF9800", fg="white")

# Run GUI
root.mainloop()
