s = input().split()
i = 1
biggest = 0
while i < len(s):
	if int(s[i]) > int(s[biggest]):
		biggest = i
	i += 1
print(s[biggest], biggest)
