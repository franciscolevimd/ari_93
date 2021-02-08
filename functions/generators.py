def natural_numbers():
	for i in [1, 2, 3]:
		yield i


def draw_triangle():
	while True:
		yield '#'


def main():
	for number in natural_numbers():
		print(number)

	column = 0
	for i in range(7):
		for pixel in draw_triangle():
			print(pixel, end='')
			if column == i:
				column = 0 
				break
			column += 1
		print('')


if __name__ == '__main__':
	main()