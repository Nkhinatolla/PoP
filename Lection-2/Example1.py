import math

def deviation(x, m):
	n = len(x)
	sum = 0
	for i in range(n):
		sum += (x[i] - m) ** 2
	return math.sqrt(sum / (n - 1))

def mean(x):
	n = len(x)
	sum = 0
	for i in range(n):
		sum += x[i]
	return (sum / n)

def main():
	line = input("Enter numbers: ").strip().split()
	List = []
	for i in range(len(line)):
		List.append(float(line[i]))
	Mean = mean(List)	
	print("The mean is ", "%.2f" % Mean)
	print("The standard deviation is", "%.5f" % deviation(List, Mean))
main()