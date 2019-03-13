import random

def main():
	D = [0] * 9
	for i in range(0, 10):
		D.append(i)
	for i in range(1000):
		x = random.randint(0, 9)
		D[x] += 1
	for i in range(0, 10):
		print(i, D[i])
main()