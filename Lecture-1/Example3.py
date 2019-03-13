	
def sumColumn(m, columnIndex):
	sum = 0
	for i in range(3):
		sum += m[i][columnIndex]
	return sum

def main():
	
	a = [[0 for x in range(4)] for y in range(3)] 
	for i in range(3):
		text = "Введите строку матрицы 3 на 4 для строки " + str(i) + ":"
		line = input(text).strip().split()
		for j in range(4):
			a[i][j] = float(line[j])
	for j in range(4):
		print("Сумма элементов для столбца " + str(j) + " равна", sumColumn(a, j))
			
main()