
def printing(s, cur) :
	for i in range(len(s)):
		if i == cur[0]:
			print(s[i][:cur[1]] + '^' + s[i][cur[1]:])
			# print(s[i][:cur[1]] + colored('^', 'red') + s[i][cur[1]:])
		else:
			print(s[i])
	print("-------------")

def cmd_r(s, cur, word):
	cur = (cur[0], s[cur[0]].rfind(word, 0, cur[1]))
	return cur

def cmd_t(s, cur):
	if (cur[1] == 0):
		return cur
	s[cur[0]] = s[cur[0]][:cur[1] - 1]  + s[cur[0]][cur[1]] + s[cur[0]][cur[1] - 1] + s[cur[0]][cur[1] + 1:]
	return cur

def cmd_plus(s, cur): 
	if (cur[0] == len(s)):
		return cur
	cur = (cur[0] + 1, 0)
	return cur

def cmd_insert(s, cur, word): 
	s[cur[0]] = s[cur[0]][:cur[1]] + word + s[cur[0]][cur[1] +1:]
	return cur
