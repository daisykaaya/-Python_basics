import random
def get_choices():
    player_choice = input("Enter your choice('rock', 'paper', 'scissors')")
    options=['rock', 'paper', 'scsissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer":computer_choice}
    return choices
choices = get_choices()
print(choices) 
