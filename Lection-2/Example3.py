def main():
	n = int(input("Enter the number of student: ").strip())
	line = input("Enter the grades of student: ").strip().split()
	a = []
	for i in range(n):
		a.append(float(line[i]))
	for i in range(n):
		for j in range(i + 1, n):
			if a[i] < a[j]:
				a[i], a[j] = a[j], a[i]
	print(a[0], a[1])
main()

