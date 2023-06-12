"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	pre_condition: users input the number check whether the is prime or not.
	post_condition: users will get the two kinds of  answer, a prime number or not a prime number.
	"""
	print('Welcome to prime checker!')
	while True:
		n = int(input('n or (' + str(EXIT) + ' to exit.): '))
		if n == EXIT:
			print('Have a good one !')
			break
		elif n == 2 or n == 3:  # 2,3 is a prime number, to avoid the situation it becomes not a prime number.
			print(str(n) + ' is a prime number.')
		elif n % 2 == 0 or n % 3 == 0:  # except 2 and 3, it will check the number if it a prime number or not.
			print(str(n) + ' is not a prime number.')
		else:
			print(str(n) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
