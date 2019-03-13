import math
def main():
	line1 = input("Enter weight and price for package 1: ").strip().split()
	line2 = input("Enter weight and price for package 2: ").strip().split()
	pkg1 = float(line1[1])
	pkg2 = float(line2[1])
	x = int(line1[0].strip(','))
	y = int(line2[0].strip(','))
	l = (x * y) / math.gcd(x, y)
	if (l / x) * pkg1 > pkg2 * (l / y):
		print("Package 1 has the better price.")
	elif (l / x) * pkg1 < pkg2 * (l / y):
		print("Package 2 has the better price.")
	else:
		print("Both equal")
main()
