"""
File: quadratic_solver.py
Name: Climent Lin
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	pre_condition: users input the numbers, a, b ,c  in the quadratic solver.
	post_condition: users will get the answer from the quadratic solver.
	"""
	print('StanCode Quadratic Solver! ')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = (b * b) - (4 * a * c)
	if d == 0:
		y = math.sqrt(d)    # first , the square root of 'd' equals y
		x = (-b + y) / (2 * a)     # second , it will only have one root while 'd == 0'
		print('One root: ' + str(x))
	elif d > 0:  			# if d(b^b - 4ac)>0 ,it will print 2 real roots
		y = math.sqrt(d)    # first , the square root of 'd' equals y
		x = (-b + y) / (2 * a)   # second , x and x_1 are the answers of two roots.
		x_1 = (-b - y) / (2 * a)
		print('Two root: ' + str(x)+','+str(x_1))
	else:    					# if d(b^b - 4ac)<0 ,it will print no real roots
		print('No real roots')


	# second solution
	# if d < 0:
	# 	print('No real roots')
	# if d > 0:
	# 	y = math.sqrt(d)
	# 	x = (-b + y) / (2 * a)
	# 	x_1 = (-b - y) / (2 * a)
	# 	print('Two root: ' + str(x)+','+str(x_1))
	# if d == 0:
	# 	y = math.sqrt(d)
	# 	x = (-b + y) / (2 * a)
	# 	print('One root: ' + str(x))


# DO NOT EDIT CODE BELOW THIS LINE

if __name__ == "__main__":
	main()
