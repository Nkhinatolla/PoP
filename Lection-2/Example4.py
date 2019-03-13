def main():
	n = int(input("Enter the number of lines: ").strip())
	for row in range(1, (n + 1)):
		for i in range(1, n - row + 1):
			print(" ", end = " ")
		for i in range(row, 1, -1):
			print (i, end = " ")
		for i in range(1, row + 1):
			print (i, end = " ")
		print() 
main()
