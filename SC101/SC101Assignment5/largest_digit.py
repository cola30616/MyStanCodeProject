"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, positive number or negative numberr
	:return: find_largest_digit_helper(n, largest_num)
	"""
	if n < 0:
		n = -n  # turn into positive number
	largest_num = 0
	return find_largest_digit_helper(n, largest_num)


def find_largest_digit_helper(n, largest_num):
	"""
	:param n : int, from find_largest_digit(n)
	:param largest_num : init is 0 , to store the largest value
	"""
	# base case
	if n == 0:  # negative digit % 10 == 0
		return largest_num
	else:
		temp_num = n % 10  # n % 10, it would be the last number in param n
		if temp_num > largest_num:  # compare the largest number
			largest_num = temp_num
		return find_largest_digit_helper(n//10, largest_num)  # each recursive divided by 10 and make floor division


if __name__ == '__main__':
	main()
