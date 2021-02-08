class CrazyIterable:
	"""Testing the iterable objects.

    Attr:
        l (tuple): Elements list.
        i (int): Current index.

    """
	l = None
	i = None


	def __init__(self, *args):
		"""Iterable object.
		Args:
		    args (tuple): Arguments list.
		"""
		self.l = args
		self.i = 0


	def __iter__(self):
		return self


	def __next__(self):
		"""Evaluates if the iterable object contains values to returns. Throws a StopIteration if the iterable object 
		has reached the end of its values.

		Returns:
        	The next value of the iterable object.
		"""
		if self.i >= len(self.l):
			self.i = 0
			raise StopIteration
		result = self.l[self.i]
		self.i += 1
		return result


def natural_numbers():
	for i in [1, 2, 3]:
		yield i


def get_pixel():
	while True:
		yield '#'


def print_prime_numbers():
	iterable_numbers = CrazyIterable(1, 3, 5, 7)
	prime_numbers = iter(iterable_numbers)
	try:
		number = prime_numbers.__next__()
		while number:
			print(number)
			number = prime_numbers.__next__()
	except:
		print('Fin')


def main():
	for number in natural_numbers():
		print(number)

	column = 0
	for i in range(7):
		for pixel in get_pixel():
			print(pixel, end='')
			if column == i:
				column = 0 
				break
			column += 1
		print('')
	print_prime_numbers()


if __name__ == '__main__':
	main()