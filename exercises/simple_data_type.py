def sum_numbers(n):
	"""Add the numbers from 1 to n.

	Args:
	    n (int): Maximum value of the sum.

	Returns:
	    int: The sum of the numbers. 
	"""
	return int((n*(n+1))/2)


def calculate_payment(salary_per_hour:float, hours_worked:float):
	"""Calculates the salary to be paid for hours worked.

	Args:
	    salary_per_hour (float): Hourly wage to be paid.
	    hours_worked (float): Hours worked to calculate the pay.

	Returns:
	    float: The salary to be paid.
	"""
	return salary_per_hour * hours_worked


def main():
	# salary = float(input('What is the hourly wage? '))
	# hours = float(input('How many hours have you worked? '))
	# payment = calculate_payment(salary, hours)
	# print(f'The payment is {payment}')

	number = int(input('Give me a number: '))
	result = sum_numbers(number)
	print(f'The sum of 1 to {number} is {result}.')


if __name__ == '__main__':
	main()