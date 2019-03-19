l = list(input().split())
mono = 0 #1 - mono. inc. 2 - mono. dec.
for i in range(1, len(l)):
	if mono == 0:
		if l[i] > l[i - 1]:
			mono = 1
		else:
			mono = 2
	elif mono == 1:
		if l[i] < l[i - 1]:
			print(i - 1, end = " ")
			mono = 2
	else:
		if l[i] > l[i - 1]:
			print(i - 1, end = " ") 
			mono = 1
