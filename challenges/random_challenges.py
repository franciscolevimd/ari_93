import numpy as np
from itertools import accumulate


def count_substrings(main_string):
	"""Count the substrings starting with A and ending with X of a main string.

	For example, given the input string "CAXAAYXZA", there are four substrings that start with "A" and end with "X", 
	which are: AX, AXAAYX, AAYX, and AYX.

	Args:
		main_string (str): Main string.

	Returns:
		int: Total substrings starting with A and ending with X.
	"""
	total_substring = 0
	main_string = main_string.upper()
	for i in range(len(main_string)):
		if main_string[i] == 'A':
			total_substring += main_string.count('X', i, len(main_string))
	return total_substring


def split_sequences():
	"""Request a sequence of words, order this sequence, and discard repeated words.
	
	Returns:
		str: Orderly sequence without repetition of words.
	"""
	sequence = input('Input a word sequence: ').upper().split()
	sort_sequence = sorted(set(sequence))
	return ' '.join(sort_sequence)


def build_square(n):
	"""Builds a square with side length n and fills the square with the value of n.

	Args:
		n (int): Side length and fill value of the square.

	Returns:
		numpy.ndarray: Matrix representing a square.
	"""
	return np.full((n, n), n)


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
	# numbers = []
	# numbers = [1, 5, 7]
	# accumulate = add_accumulated(numbers)
	# print(f'Numbers: {numbers}')
	# print(f'Accumulate: {accumulate}')

	# n = None
	# square = build_square(n)
	# print(f'Square[{n}x{n}]\n{square}')

	#print(split_sequences())

	input_string = input('Give me a string: ')
	print(f'The total of substrings on {input_string.upper()} is {count_substrings(input_string)}.')


if __name__ == '__main__':
	main()