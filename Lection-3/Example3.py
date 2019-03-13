def main():

	file = input("Enter a filename: ")
	f = open(file, "r")
	text = f.readline().split()
	f.close()
	print("There are", len(text), "scores")
	total = 0
	for i in text:
		total += int(i)
	print("There total is", total)
	print("The average is", total / len(text))	

main()