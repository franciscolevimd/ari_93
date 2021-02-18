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
	word = 'Reconocer'
	if is_palindorme(word):
		print(f'{word} is a palindrome.')
	else:
		print(f'{word} isn\'t a palindrome.')


if __name__ == '__main__':
	main()