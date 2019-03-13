import math
def mean(x):
	sum = 0
	for i in range(len(x)):
		sum += float(x[i])
	return sum / len(x)
def deviation(x):
	sum2 = 0
	for i in range(len(x)):
		sum2 += (float(x[i]) - mean(x)) ** 2
	return((sum2 / (len(x) - 1)) ** 0.5)
def main():
	a = input("Enter ").strip().split()
	print('%.2f' % mean(a))
	print('%.5f' % deviation(a))
	#print(math.sqrt(sum2 / (len(a) - 1)))
main()