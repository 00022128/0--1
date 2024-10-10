import random

print('Welcome to Guess a number game !')
print('Here are the simple rules of this game:\n1. Guess a number from 1 to 100\n2. You are given only 5 attempts\n3. Good luck !')
name = input('Enter your name: ')

while True:
    try:
        random_number = random.randint(1, 100)
        attempt = 5
    except ValueError:
        print('Invalid input, please enter a number !')
        continue

    while attempt > 0:
        num = int(input('Guess a number from 1 to 100: '))
        if num > random_number:
            attempt -= 1
            print(f'{num} is too High !\nAttempts left: {attempt}')
        elif num < random_number:
            attempt -= 1
            print(f'{num} is too Low !\nAttempts left: {attempt}')
        elif num == random_number:
            print(f'Congrats {name} ! You guessed the number correctly!\nAttempts left: {attempt}')
            play_again = input('Would you like to play again? (y/n) ').lower()
            if play_again == 'y':
                random_number = random.randint(1, 100)
                attempt = 5
            if play_again != 'y':
                print(f'Thank you for playing! {name}')
                break
    if attempt == 0:
        print(f'You lost ! {name}')
        play_again = input('Would you like to play again? (y/n) ')
        if play_again == 'y':
            random_number = random.randint(1, 100)
            attempt = 5
        if play_again != 'y':
            print(f'Thank you for playing! {name}')
            break


