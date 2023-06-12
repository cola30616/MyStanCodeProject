"""
File: extension1_factorial.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	pre_condition: user input the number to know the answer of factorial.
	post_condition: user gets the answer of factorial.
	"""
	print('Welcome to stanCode factorial master! ')
	n = int(input('Give me a number, and I will list the answer of factorial: '))
	n1 = 1
	while n != 0:
		if n == EXIT:  # if the number == EXIT, it will end up the loop.
			print('- - - - - - See ya! - - - - - -')
			break
		if n > 0:
			n1 = n1 * n  # n1 will be re-assign and get the value of factorial
			n -= 1
		if n == 0:  # if n == 0 , it will print the answer of factorial.
			print('Answer:' + str(n1))
			n = int(input('Give me a number, and I will list the answer of factorial: '))
			n1 = 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()