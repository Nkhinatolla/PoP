l = list(input().split())
mx = 0
ans = None
for i in l:
	if l.count(i) > mx:
		ans = i
		mx = l.count(i)
print(ans)