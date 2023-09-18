import random

# Define the possible choices
choices = ["rock", "paper", "scissors"]

# Get the user's choice
user_choice = input("Choose rock, paper, or scissors: ")

# Get the computer's choice
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
  print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
  print("Rock beats scissors! You win!")
elif user_choice == "paper" and computer_choice == "rock":
  print("Paper beats rock! You win!")
elif user_choice == "scissors" and computer_choice == "paper":
  print("Scissors beats paper! You win!")
else:
  print("Computer wins!")