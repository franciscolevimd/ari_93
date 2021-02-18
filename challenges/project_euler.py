def sum_multiples_3_5(max_number = 10):
	"""Find the sum of all the multiples of 3 or 5 below max_number.

	Args:
	    max_number (int): Calculates the sum below this number. Default is 10.

	Returns:
	    int: Sum of all the multiples of 3 or 5 below max_number.
	"""
	result = 0
	for number in range(1, max_number):
		if number % 3 == 0 or number % 5 == 0:
			result += number
	return result


def main():
	# Find the sum of all the multiples of 3 or 5 below 1000.
	print(sum_multiples_3_5(1000))


if __name__ == '__main__':
	main()