def main():
	fee = 10000;
	for i in range(10):
		fee = fee + fee * 0.05;
	print("The tuition in ten years:", round(fee, 4));
	sum = 0;
	for i in range(4):
		sum += fee;
		fee = fee + fee * 0.05;
	print("The total cost of four years:", round(sum, 4));
main() 