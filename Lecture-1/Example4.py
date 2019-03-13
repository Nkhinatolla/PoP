def main():
	line = input("Введите 10 чисел:").strip().split()
	a = []
	for i in range(10):
		if not int(line[i]) in a: 

			a.append(int(line[i]))
	print("Отдельные (неповторяющиеся) числа: ", end = "")
	for i in range(len(a)):
		print(a[i], end = " ")
main()