import time 
import math
import pyperclip as clipboard


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


def sum_even_fibonacci_numbers(max_number = 10):
	"""Sum the even-valued terms of the Fibonacci sequence.

	Args:
	    max_number (int): Max value of the terms.

	Returns:
	    int: Result of sum of the even-valued terms of the Fibonacci sequence whose maximum value is max_number. 
	"""
	result = 0
	x, y = 1, 2
	while True:
		if x % 2 == 0:
			result += x
		x, y = y, y + x
		if x >= max_number:
			break
	return result


def eratosthenes_sieve(n=10):
	"""Generates the eratosthenes sieve of all numbers less than or equal to n.

	Args:
	    n (int): Maximum number of the sieve. Default is 10.

	Returns:
	    list: The eratosthenes sieve of all numbers less than or equal to n.
	"""
	sieve = list()
	multiples = set()
	for i in range(2, n+1):
		if i not in multiples:
			multiples.update(range(i*i, n+1, i))
			sieve.append(i)
		multiples.discard(i)
	return sieve


def is_prime(number):
	"""Determines if a number is prime.

	Args:
	    number (int): Number to evaluate.

	Returns:
	    bool: True if number is prime else False.
	"""
	if number == 2:
		return True	
	elif number % 2 == 0:
		return False
	else:
		criba = eratosthenes_sieve(int(math.sqrt(number)))
		for prime in criba:
			if number % prime == 0:
				return False
		else:
			return True
	

def factorize_division(number):
	"""Generates the factors of a number by division method.

	Args:
	    number (int): Number to factorize.

	Returns:
	    int: the next factor of the number.
	"""
	for i in range(2, number):
		if is_prime(i):
			while True:
				if number % i == 0:
					yield i
					number = number / i
					if number == 1:
						break
				else:
					break
		if number == 1:
			break


def fermat_factors(number):
	"""Generates the two largest factors of a number by the Fermat algorithm.

	Args:
	    number (int): Number to factorize.

	Returns:
	    list: The two largest factors of the number.
	"""	
	if number & 1 == 0:
		return [number // 2, 2]
	a = math.ceil(math.sqrt(number))
	if a * a == number:
		return [a, a]
	while True:
		b1 = a*a - number
		b = int(math.sqrt(b1))
		if b*b == b1:
			break
		else:
			a += 1
	return [a-b, a+b]


def factorize(number):
	"""Factorize a number.

	Args:
	    number (int): Number to factorize.

	Returns:
	    list: Factors of the number.
	"""	
	factors = []
	if number == 2 or is_prime(number):
		factors.append(number)
		return factors
	if number < 100_000:
		for factor in factorize_division(number):
			factors.append(factor)
	else:
		f = []
		factors = fermat_factors(number)
		for i in range(len(factors)):
			f += factorize(factors[i])
		f.sort()
		factors = f
	return factors


def main():
	start = time.time()

	# Find the sum of all the multiples of 3 or 5 below 1000.
	# print(sum_multiples_3_5(1000))
		
	# Find the sum of the even-valued terms considering the Fibonacci sequence whose values do not exceed four million.
	# max_number = 4000000
	# print(f'Max value of the terms: {max_number}')
	# sum_fibonacci = sum_even_fibonacci_numbers(max_number)
	# clipboard.copy(sum_fibonacci)
	# print(sum_fibonacci)

	# number = 600_851_475_143
	# factors = factorize(number)
	# print(f'Prime factors of {number}: {factors}') # [71, 839, 1471, 6857]

	# prime_generator = factorize_division(81)
	# print(next(prime_generator))

	# print(fermat_factors(261_405_929)) # [15773, 16573]

	end = time.time()
	print(f'Execution time: {round((end - start) / 60, 2)} minutes') 


if __name__ == '__main__':
	main()