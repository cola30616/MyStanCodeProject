"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -1


def main():
	"""
	pre_condition: user input the temperature, input the QUIT number to exit
	post_condition: user will get the highest,lowest, average of the temperature,
					if the temperature < 16, it will count and show how many cold days.
	"""
	print("""stanCode "Weather Master 4.0" ! """)
	data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
	if data == QUIT:  # this is the first number
		print('No temperature were entered')
	else:
		maximum = minimum = average = data  # if only input one number, all the values are the same.
		count = 1  # this value is to count how many days
		cold = 0   # this value is to count how many cold days
		if data < 16:
			cold += 1
		while True:
			data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
			if data == QUIT:
				break
			if data > maximum:  # if the latter number is bigger than the former number, it become the maximum.
				maximum = data
			if data < minimum:  # if the latter number is lower than the former number, it become the minimum.
				minimum = data
			if data != QUIT:
				average += data  # it will add all the temperature value
				count += 1  # this value is to count how many days
			if data < 16:  # if the temperature < 16 , it will count the cold day.
				cold += 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average/count))  # to get the value of average
		print(str(cold) + ' cold day(s).')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
