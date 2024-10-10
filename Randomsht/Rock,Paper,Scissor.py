"""Rock, Paper Scissor game !"""

import random

options = ('rock', 'paper', 'scissor')
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice ! (rock, paper, scissor): ").lower()
    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print('Tie')
    elif player == 'rock' and computer == 'scissor':
        print("You win!")
    elif player == 'paper' and computer == 'rock':
        print("You win!")
    elif player == 'scissor' and computer == 'paper':
        print("You win!")
    else:
        print("You lose!")
    while True:
        play_again = input('Do you wish to play again? (y/n): ').lower()
        if play_again in ('y', 'n'):
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

        # If the player chooses 'n', stop the game
    if play_again == 'n':
        running = False

print('Thanks for playing!')