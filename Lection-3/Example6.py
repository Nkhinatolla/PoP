def main():
	n = 8
	for row in range(n):
		for space in range(n - row - 1):
			print('{:>4}'.format(" "), end = "")
		for x in range(row + 1):
			print('{:>4}'.format(2 ** x), end = "")
		x = 2 ** row
		for i in range(row):
			x = int(x / 2)
			print('{:>4}'.format(x), end = "")	
		print()
main()

# row = 3
