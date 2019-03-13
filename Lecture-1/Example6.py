def main():
	line = input("Введите баллы: ").strip().split()
	List = []
	maxPoint = 0
	for i in range(len(line)):
		List.append(int(line[i]))
		maxPoint = max(maxPoint, List[i])
	for i in range(len(List)):
		print("Студент", i, "балл", List[i], "оценка", end = " ")
		if maxPoint - List[i] <= 10:
			print("A")
		elif maxPoint - List[i] <= 20:
			print("B")
		elif maxPoint - List[i] <= 30:
			print("C")
		elif maxPoint - List[i] <= 40:
			print("D")
		else:
			print("F")


main()