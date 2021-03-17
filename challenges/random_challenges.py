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

	numbers = None	
	sort_numbers = sort_only_natural_numbers(numbers)
	print(f'Original list: {numbers}')
	print(f'Sort list: {sort_numbers}')


if __name__ == '__main__':
	main()