file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")
file3 = open("file3.txt", "w")
for i, j in zip(file1, file2):
	i = i[:len(i) - 1]
	j = j[:len(j) - 1]
	file3.write(i + " " + j + "\n")
file3.close()
file1.close()
file2.close()