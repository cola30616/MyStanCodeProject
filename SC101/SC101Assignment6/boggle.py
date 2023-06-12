"""
File: boggle.py
Name: Clement
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	print('Please type 4 letters with blank space in each row. e.g: f y c l')
	letter_list = user_input()
	start = time.time()
	if len(letter_list) == 4:
		word_search(letter_list)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def user_input():
	letter_list = []
	for i in range(4):
		row = input(f'{i+1} row of letters: ').lower()
		if len(row) != 7:
			print('illegal input')
			break
		letter = row.split()
		letter_list.append(letter)
	return letter_list


def word_search(letter_list):
	"""
	:param letter_list: usr input four rows of letter
	:return:  None
	"""
	all_txt = read_dictionary()
	ans_list = []
	# [f, y, c, l]
	# [i, o, m, g]
	# [o, r, i, l]
	# [h, j, h, u]
	for i in range(len(letter_list)):  # use double for loop to choose only one letter
		for j in range(len(letter_list[i])):
			row = i
			col = j
			duplicated_coordinate = [(row, col)]
			# 1. choose one letter, use recursion to search its neighbor letter
			word_search_helper(letter_list, row, col, duplicated_coordinate, letter_list[i][j], ans_list, all_txt)
	print(f'There are {len(ans_list)} word in total')


def word_search_helper(letter_list, row, col, coordinate, word_searched, ans_list, all_txt):
	"""
	:param letter_list:  users input
	:param row: double for loop (i)
	:param col: double for loop (j)
	:param coordinate: store the (dx, dy) that have been used
	:param word_searched: startswith the letter letter_list[i][j]
	:param ans_list: words have been searched store in the list
	:param all_txt: a list that store all words from dict
	:return:  ans_list
	"""
	# base case
	if word_searched in all_txt and word_searched not in ans_list:
		ans_list.append(word_searched)
		print(f'Found {word_searched}')
	# recursion
	# i don't know how to find roomy :(
	else:
		for i in range(-1, 2, 1):  # The algorithm in Assignment 0 blur.py
			for j in range(-1, 2, 1):
				dx = row + i
				dy = col + j
				# choose
				if (dx, dy) not in coordinate:  # avoid the duplicated coordinate
					if 0 <= dx <= 3 and 0 <= dy <= 3:  # avoid out of range
						word_searched += letter_list[dx][dy]
						coordinate.append((dx, dy))
					# explore
						if has_prefix(word_searched, all_txt):
							word_search_helper(letter_list, dx, dy, coordinate, word_searched, ans_list, all_txt)
					# un choose
						coordinate.pop()
						word_searched = word_searched[:-1]
		return ans_list


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	all_txt = []
	with open(FILE, 'r') as f:
		for word in f:
			clean_word = word.strip()
			if 4 <= len(clean_word) <= 16:   # The letters is between in 4 to 16
				all_txt.append(clean_word)
	return all_txt


def has_prefix(sub_s, all_txt):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param all_txt: an array that store the word from the dict
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in all_txt:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
