import random
def get_choices():
    player_choice = input("Enter your choice('rock', 'paper', 'scissors')")
    options=['rock', 'paper', 'scsissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose  {player} Computer chose  {computer}")
    if player == computer:
        return "it's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rocks smarshes scissors. You Win!"
        else: 
            return "Papers cover rocks! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else: "Scissors cut paper! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else: 
            return "Rock smarshes scissors! You lose!"
choices = get_choices()