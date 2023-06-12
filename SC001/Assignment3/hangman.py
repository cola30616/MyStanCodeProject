"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    pre_condition: user have 7(constant) chances to guess the word
    post_condition: if win, it will show the answer and 'you win'
                    if lose, it will show you are already hung
    """
    play()


def play():
    chance = N_TURNS  # int , the constant number .
    word = random_word()  # str , the word is from 'def random word()'.
    ans = len(word) * '-'  # str , the word is replaced by '-'.
    while True:
        print('The word looks like ' + ans)
        print('You have ' + str(chance) + ' wrong guesses left.')
        guess = input('Your guess: ').upper()  # guess will be change to upper case.
        if len(guess) != 1 or not guess.isalpha():  # if the guess is number or user type more than 2 letters,
            print('Illegal format')             # print illegal format
        elif guess not in word:
            print('There is no ' + guess + "'s in the word")    # if guess not in the word, it will show not that word.
            chance -= 1  # the chance minus 1
        else:
            print('You are correct!')  # if guess is in the word
            old_word = ans  # old_word = to retain the answer previous.
            ans = ''
            for i in word:  # i= each letter from the word
                if guess == i:  # if the guess and the letter of the word are the same.
                    ans += guess  # it will add the guess in the answer.
                else:
                    i_1 = word.find(i)  # if not, it will search the position of word.
                    ans += old_word[i_1]  # it will add the letter of old word in the answer.
        if chance == 0:
            print('You are completely hung. :(')
            break  # run out of the chance , the game is over
        elif ans == word:
            print('You win!!')
            print('The word was: ' + str(ans))
            break  # find the word, the game is over.


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
