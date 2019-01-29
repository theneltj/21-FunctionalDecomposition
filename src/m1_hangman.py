"""
Hangman.

Authors: Tyler Thenell and Zachary Zdanavicius.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
import random
####### Do NOT attempt this assignment before class! #######


def main():
    print('_________________________________')
    print('|           -HANGMAN-            |')
    print('|         Tyler & Zach           |')
    print('|________________________________|')
    min_length = int(input('Give a minimum length: '))
    num_guesses = int(input('How many chances do you want: '))
    secret_word = word_selector(min_length)
    guessing_runner(secret_word, num_guesses)


def word_selector(minimum):
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        word = string.split()
        r = random.randrange(0, len(word))
        item = word[r]
        while True:
            if len(item) >= minimum:
                return item


def print_known(secret_word, guessed):
    print()
    for k in range(len(secret_word)):
        for j in range(len(guessed)):
            if secret_word[k] == guessed[j]:
                print(secret_word[k], end='')
                break
            if j+1 == len(guessed):
                print('_ ', end='')


def guessing_runner(secret_word, num_guesses):
    guessed = ''
    num_guessed = 0
    while num_guessed < num_guesses:
        print_known(secret_word, guessed)
        print()
        print('You have', num_guesses - num_guessed, 'tries left!')
        print('And have guessed: ', guessed)
        new_guess = input('Enter your new guess: ')
        if len(new_guess) == 1:
            guessed += new_guess

        for k in range(len(secret_word)):
            if secret_word[k] == new_guess:
                num_guessed -= 1
                break

        num_guessed += 1
        if win_check(secret_word, guessed) == True:
            results(True, secret_word)
            return

    results(False, secret_word)


def win_check(secret_word, guessed):
    checker = ''
    for k in range(len(secret_word)):
        for j in range(len(guessed)):
            if secret_word[k] == guessed[j]:
                checker += guessed[j]
                break
    if secret_word == checker:
        return True
    return False


def results(result, secret_word):
    for k in range(10):
        print()
    print(' __________________')
    if result == True:
        print('|     YOU WIN!     |')
    if result == False:
        print('|     YOU LOSE     |')
    print('|__________________|')
    print('The word was: ', secret_word)

main()
