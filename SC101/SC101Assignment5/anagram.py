"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        target_word = input('Find anagrams for: ').lower()
        start = time.time()
        if target_word == EXIT:
            break
        else:
            find_anagrams(target_word)
            end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(target_word):
    """
    :target_word =  user input
    this dict only remains the same length of the word, it will loop really quickly
    """
    all_txt = []
    with open(FILE, 'r') as f:
        for line in f:
            if len(target_word) + 1 == len(line):  # the same length of word will append into the all_txt
                word = line.replace('\n', '')  # str manipulation to remove '\n'
                all_txt.append(word)
    return all_txt


def find_anagrams(s):
    """
    :param s: user input
    """
    all_txt = read_dictionary(s)
    print('Searching')
    ans = find_anagrams_helper(s, '', [], all_txt)
    print(f'{len(ans)} anagrams: {ans}')  # 原本使用counter 計算次數, 寫起來太過冗長，後來想到可以修改成這樣


def find_anagrams_helper(s, searching_word, searching_list, all_txt):
    """
    :param s: user input
    :param searching_word: an empty str, to check the word that we wanna find in the dict
    :param searching_list: to store each word has been found in the dict
    :param all_txt: read_dictionary()
    """
    # base case
    if len(s) == len(searching_word):  # length of input is the same as the searching word
        if searching_word not in searching_list:  # to check the word is in the list or not
            searching_list.append(searching_word)
            print(f'Found: {searching_word}')
            print('Searching')  # to make sure the user know it is still running
    # recursion
    else:
        for letter in s:
            #  count() I ask one of my friend studied in CS. He taught me this way to calculate the times of each letter
            if letter in searching_word and searching_word.count(letter) == s.count(letter):
                pass
            else:
                # choose
                searching_word += letter
                # explore
                if has_prefix(searching_word, all_txt):  # True: continue to search, False: move to undo
                    find_anagrams_helper(s, searching_word, searching_list, all_txt)
                # un - choose
                undo = list(searching_word)  # make letter become a list, and use the method pop()
                undo.pop()  # undo , go back to the previous str
                searching_word = ''.join(undo)
    return searching_list


def has_prefix(sub_s, all_txt):
    """
    :param sub_s: the current searching word
    :param all_txt: read_dictionary()
    :return: boolean, true or False
    """
    for word in all_txt:  # if sub_s is the same, it will continue to search
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
