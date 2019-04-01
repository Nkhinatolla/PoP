def printing(s, cur) :
	print(s[:cur] + '^' + s[cur:])
	print("-------------")

def cmd_r(s, cur, word):
	cur = s.rfind(word, 0, cur)
	return cur

def cmd_t(s, cur):
	if (cur == 0):
		return s
	s = s[:cur - 1]  + s[cur] + s[cur - 1] + s[cur + 1:]
	return s

def cmd_insert(s, cur, word): 
	s = s[:cur] + word + s[cur:]
	return s