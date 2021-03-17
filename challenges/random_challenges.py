from itertools import accumulate


def add_accumulated(numbers):
	"""Returns the add accumulate of each element of a list numbers.

	Example: 
	
		In:[1, 5, 7]
		Out: [1, 6, 13]

	Args:
		numbers (list): Number list.

	Returns:
		list: Cumulative sum list.
	"""
	# Solution 1
	# result = []
	# accumulated = 0
	# for number in numbers:
	# 	accumulated += number
	# 	result.append(accumulated)
	# return result
	# Solution 2
	# return [sum(numbers[:i + 1]) for i in range(len(numbers))]
	# Solution 3
	return list(accumulate(numbers))



def sort_only_natural_numbers(numbers):
	"""Sort only the natural numbers within a list. The remaining numbers will remain in their original position

	Args:
		numbers (list): Original number list.

	Returns:
		list: The list with the natural numbers ordered.
	"""
	natural_numbers = sorted([number for number in numbers if number > 0], reverse=True)
	return [natural_numbers.pop() if number > 0 else number for number in numbers]


def is_palindorme(word):
	"""Valid if a word is a palindrome.

	Args:
	    word (str): Word to validate.

	Returns:
	    bool: True if the word is a palindrome else returns False.
	"""
	upper_word = str.upper(word)	
	return upper_word == upper_word[::-1]


def main():
	# word = 'Tania'
	# word = 'Reconocer'
	# if is_palindorme(word):
	# 	print(f'{word} is a palindrome.')
	# else:
	# 	print(f'{word} isn\'t a palindrome.')

	# numbers = None	
	# sort_numbers = sort_only_natural_numbers(numbers)
	# print(f'Original list: {numbers}')
	# print(f'Sort list: {sort_numbers}')

	# numbers = None
	numbers = []
	# numbers = [1, 5, 7]
	accumulate = add_accumulated(numbers)
	print(f'Numbers: {numbers}')
	print(f'Accumulate: {accumulate}')


if __name__ == '__main__':
	main()