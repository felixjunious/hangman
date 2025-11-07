import random

from hangman_art import HANGMANPICS, logo
from hangman_words import word_list

print(logo)

lives = 6

chosen_words = random.choice(word_list)
print(chosen_words)

placeholder = '_' * len(chosen_words)

print('Word to guess:', placeholder)

game_over = False
correct_letters = set()

while not game_over:
    print(f'========================={lives}/6 LIVES LEFT=========================')
    guess = input('Guess a letter: ').lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ''

    for letter in chosen_words:
        if letter == guess:
            display += letter
            correct_letters.add(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print('Word to guess:', display)

    if guess not in chosen_words:
        lives -= 1
        print(f"You guesses {guess}, that's not in the word. You lose a life")

        if lives == 0:
            game_over = True

            print(f'=========================IT WAS {chosen_words}! YOU LOSE=========================')

    if '_' not in display:
        game_over = True
        print('=========================YOU WIN=========================')

    print(HANGMANPICS[6-lives])
