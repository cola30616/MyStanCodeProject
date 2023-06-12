"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    pre_condition: user type how many steps need to move and the word of caesar.
    post_condition: user get the word which is deciphered.
    """
    move_number = int(input('Secret number: '))
    old_string = input('What is the ciphered string? ').upper()
    print('The deciphered string is: ' + the_deciphered_string(move_number, old_string))


def the_deciphered_string(move_number, old_string):
    """
    :param move_number: int , the number to be valued.
    :param old_string: str ,  the previous string to be valued.
    :return: str, the answer of the deciphered _string.
    """
    ans = ''
    na = ALPHABET[len(ALPHABET)-move_number:len(ALPHABET)]  # na = how many letter need to move
    na_1 = ALPHABET[:len(ALPHABET)-move_number]  # na_2 = the rest of letter
    na_2 = na + na_1  # na_2 = New_Alphabet(already moved)
    for i in old_string:
        if i.isupper():
            i_1 = na_2.find(i)  # find the position in the New_Alphabet
            i_2 = ALPHABET[i_1]  # find the position in the constant
            ans += i_2  # add the letter in the answer.
        else:
            ans += i  # add the empty str or !. ,etc.

    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
