import random

print('Welcome to Guess a number game !')
print('Here are the simple rules of this game:\n1. Guess a number from 1 to 100\n2. You are given only 5 attempts\n3. Good luck !')
name = input('Enter your name: ')

while True:
    try:
        random_number = random.randint(1, 100)
        attempt = 5
        guesses = 0
    except ValueError:
        print('Invalid input, please enter a number !')
        continue
    game_mode = input("Do you want easy mode or hard mode ? (1 or 2) I for more info\n"
                      "q to quit: ").lower()
    if game_mode == '1':
        print("-----You have selected easy mode-----")
        is_running = True
        while is_running:
            num = int(input('Guess a number from 1 to 100: '))
            if num > 100 or num < 1:
                print('Please enter a number from 1 to 100')
                continue
            elif num > random_number:
                print(f'{num} is too high!')
                guesses += 1
            elif num < random_number:
                print(f'{num} is too low!')
                guesses += 1
            else:
                print(f'Congrats {name} ! You guessed the number correctly!\nNumber of guesses: {guesses}')
                play_again = input('Would you like to play again? (y/n) ').lower()
                if play_again == 'y':
                    random_number = random.randint(1, 100)
                elif play_again != 'y':
                    print(f'Thank you for playing! {name}')
                    break
    elif game_mode == '2':
        print("-----You have selected hard mode-----")
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
    elif game_mode == 'i':
        print('If you select easy mode, you will have unlimited attempts to find the appropriate number\n'
              'If you select hard mode, you will have limited attempts (only 5) to find the appropriate number\n')
        continue
    elif game_mode == 'q':
        break








