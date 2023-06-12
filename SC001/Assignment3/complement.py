"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    pre_condition: user type the original DNA, only type A,T,C,G.
    post_condition: user get the complement of DNA.
    """
    print(build_complement('ATC'))  # lower case or upper case is available.
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    :param dna: str, type ,A,T,C,G to check DNA.
    :return: the answer of the complement.
    """
    ans = ''
    for i in range(len(dna)):
        if dna[i].upper() == 'A':
            ans += 'T'
        elif dna[i].upper() == 'T':
            ans += 'A'
        elif dna[i].upper() == 'C':
            ans += 'G'
        elif dna[i].upper() == 'G':
            ans += 'C'
    if ans == '':
        ans += 'DNA strand is missing'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
