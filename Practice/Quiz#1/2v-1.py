s1, s2 = input().split()
l1 = []
for i in s1:
	l1.append(i)
l1.sort()
ans = False
for i in range(len(s2)):
	substr = s2[i:i + len(s1)]
	l2 = []
	for j in substr:
		l2.append(j)
	l2.sort()
	if l1 == l2:
		ans = True
		break
print(ans)