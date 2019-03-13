def main():

	answers = [
		['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
		['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
		['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
		['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
		['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
		['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
		['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
		['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
	keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

	student = [0] * 8
	ids = [0] * 8
	
	for i in range(len(answers)): # 8 students
		correctCount = 0
		for j in range(len(answers[i])):
			if answers[i][j] == keys[j]:
				correctCount += 1
		student[i] = correctCount
		ids[i] = i
		#print("Student", str(i) + "'s correct count is", correctCount)
	
	for i in range(8):
		for j in range(i, 8):
			if student[i] > student[j]:
				student[i], student[j] = student[j], student[i]
				ids[i], ids[j] = ids[j], ids[i]
	
	for i in range(8):
		print("Student", str(ids[i]) + "'s correct count is", student[i])

main()