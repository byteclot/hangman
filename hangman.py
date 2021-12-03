import random
import string

print("H A N G M A N")

choice = input('Type "play" to play the game, "exit" to quit: ')

while choice != "exit":
    secrets = ['python', 'java', 'kotlin', 'javascript']
    secret = random.choice(secrets)
    # print(secret)
    hint = '-' * len(secret)
    correct_guessed_letters = []
    all_guessed_letters = []
    wrong_count = 0
    while wrong_count < 8:
        print()
        print(hint)
        letter = input(f'Input a letter: ')
        # if letter == 'exit':
        #     choice = 'exit'
        #     break
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
            continue
        if letter not in all_guessed_letters and letter not in secret:
            print("That letter doesn't appear in the word")
            wrong_count += 1
        else:
            if letter in all_guessed_letters:
                print("You've already guessed this letter")
                # wrong_count += 1
            else:
                correct_guessed_letters.append(letter)
                hint = [a if a in correct_guessed_letters else '-' for a in secret]
                hint = ''.join(hint)
        all_guessed_letters.append(letter)
        if hint == secret:
            break

    if hint == secret:
        print("You survived!")
    else:
        print("You lost!")
    new_choice = ''
    while new_choice not in ['play', 'exit']:
        new_choice = input('Type "play" to play the game, "exit" to quit: ')
    choice = new_choice
