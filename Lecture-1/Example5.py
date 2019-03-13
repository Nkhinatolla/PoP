def main():
	line = input("Введите числа от 1 до 100:").strip().split()
	List = {i : 0 for i in range(1, 101)}
	for i in range(len(line)):
		List[int(line[i])] += 1
	for i in range(1,101):
		if List[i] != 0:
			print(i, "упоминается (встречается)", List[i], end = " ")
			if List[i] > 1:
				print ("раза")
			else:
				print ("раз")

main()