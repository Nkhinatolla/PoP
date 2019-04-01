l = input().split()
m = 1000000
for i in l: 
	if (int(i) > 0):
		m = min(m, int(i))
print(m)