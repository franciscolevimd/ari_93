def average(*numbers):
	sum = 0
	for number in numbers:
		sum += number
	return sum / len(numbers)


def max(**elements):
	values = list(elements.values())
	keys = list(elements.keys())
	if values[2] < values[0] > values[1]:
		return keys[0]
	elif values[0] < values[1] > values[2]:
		return keys[1]
	elif values[0] < values[2] > values[1]:
		return keys[2]
	return None


def main():
	#average_score = average(1, 2, 3, 4)
	#print(f'Average score: {average_score}')
	higher_value = max(b=-6, w=38, f=46)
	print(f'Higher value: {higher_value}')


if __name__ == '__main__':
	main()