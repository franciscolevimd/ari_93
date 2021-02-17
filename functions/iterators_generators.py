import itertools


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
	# for number in prime_numbers:
	# 	print(number)
	try:
		number = prime_numbers.__next__()
		while number:
			print(number)
			number = prime_numbers.__next__()
	except:
		print('Fin')


def sort_sequence(sequence):
	if len(sequence) == 0: return
	positions = []
	actual = sequence[0]
	temp = 0	
	while len(positions) < len(sequence):
		for j in range(len(sequence)):
			if actual < sequence[j] and j not in positions:
				actual = sequence[j]
				temp = j
		positions.append(temp)
		yield actual
		actual = -1


def fibonnaci():
	x, y = 0, 1
	while True:
		yield x
		x, y = y, y + x


def main():
	# for number in natural_numbers():
	# 	print(number)

	# column = 0
	# for i in range(7):
	# 	for pixel in get_pixel():
	# 		print(pixel, end='')
	# 		if column == i:
	# 			column = 0 
	# 			break
	# 		column += 1
	# 	print('')

	# print_prime_numbers()

	print([number for number in sort_sequence([1,43,2,6,0,12,4,22,5,2])]) 

	# print(list(itertools.islice(fibonnaci(), 10)))


if __name__ == '__main__':
	main()