x = int(input())
def f(y):
	print(y, end = " ")
	if (y >= 1):
		f(y - 1)
f(x)
