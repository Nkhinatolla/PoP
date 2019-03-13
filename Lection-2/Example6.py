def main():
	d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	m = int(input("Enter month: ").strip())
	y = int(input("Enter year: ").strip())
	ans = 0;
	if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
		if m == 2:
			ans = 29 	
		else:
			ans = d[m]
	else:
		ans = d[m]
	print("В", m, "месяце", ans, "дней")
main()