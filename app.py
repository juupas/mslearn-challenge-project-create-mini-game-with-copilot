# Ask for user input, allowing only rock, paper, or scissors and warn if invalid input is given
# Generate a random choice for the computer
# Compare the user's choice and the computer's choice
# Print the result of the game
# Ask if the user wants to play again
# If the user wants to play again, restart the game, otherwise exit
# After the exit, display how many games the user won, lost, and tied

import random

def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "You lose!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "You lose!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "You lose!"
    
def main():
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}. The computer chose {computer_choice}.")
        result = compare_choices(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            wins += 1
        elif result == "You lose!":
            losses += 1
        else:
            ties += 1
        
        if not play_again():
            break
    
    print(f"You won {wins} games, lost {losses} games, and tied {ties} games.")

def play_again():
    while True:
        user_input = input("Do you want to play again? (yes/no): ").lower().strip()
        if user_input == "yes":
            return user_input
        elif user_input == "no" or user_input == "":
            return False
        else:
            print("Invalid input. Please enter 'yes', 'no', or leave it empty to exit.")

if __name__ == "__main__":
    main()
