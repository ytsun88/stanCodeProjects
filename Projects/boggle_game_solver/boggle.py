"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	board = []
	li = []
	for i in range(4):
		row = input(f"{i + 1} row of letters: ")
		row = row.lower()
		check_validity(row)
		board.append(list(row.replace(' ', '')))
		li += list(row.replace(' ', ''))
	start = time.time()
	dictionary = read_dictionary(li)
	ans = []
	for row in range(4):
		for col in range(4):
			check = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
			check[row][col] = 1
			ans += find_words(board, row, col, board[row][col], [], dictionary, check)
	print(f"There are {len(ans)} words in total.")
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(li):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = set()
	s = set(li)
	with open(FILE, 'r') as f:
		for line in f:
			token = line.strip()
			if len(token) > 3:
				if check_word(token, s):
					dictionary.add(token)
	return dictionary


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


def check_validity(row):
	if len(row.replace(' ', '')) != 4:
		print("Illegal input")
		exit(0)
	if row[1] != " " or row[3] != " " or row[5] != " ":
		print("Illegal input")
		exit(0)


def find_words(board, row, col, cur_s, result, dictionary, check):
	if cur_s in dictionary and cur_s not in result:
		print("Found: " + cur_s)
		result.append(cur_s)
		if has_prefix(cur_s, dictionary):
			find_words(board, row, col, cur_s, result, dictionary, check)
	else:
		for i in range(row - 1, row + 2):
			for j in range(col - 1, col + 2):
				if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or (i == row and j == col):
					pass
				else:
					if check[i][j] == 0:
						cur_s += board[i][j]
						check[i][j] = 1
						if has_prefix(cur_s, dictionary):
							find_words(board, i, j, cur_s, result, dictionary, check)
						cur_s = cur_s[:-1]
						check[i][j] = 0
	return result


def check_word(word, li):
	for c in word:
		if c not in li:
			return False
	return True


if __name__ == '__main__':
	main()
