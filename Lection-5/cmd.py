from colorama import init
from termcolor import colored
init()
def cmd_h(s, cur):
	if (cur[1] > 0):
		cur = (cur[0], cur[1] - 1)
	return cur

def cmd_i(s, cur):
	if (cur[1] < len(s[cur[0]]) - 1):
		cur = (cur[0], cur[1] + 1)
	return cur
def cmd_j(s, cur):
	if (cur[0] > 0):
		cur = (cur[0] - 1, cur[1])
	return cur

def cmd_k(s, cur):
	if (cur[0] < len(s) - 1):
		cur = (cur[0] + 1, cur[1])
	return cur

def cmd_x(s, cur):
	if (cur[1] != 0):
		ss = s[cur[0]]
		s[cur[0]] = ss[:cur[1] - 1] + ss[cur[1]: ]
		cur = (cur[0], cur[1] - 1)
	return cur

def cmd_d(s, cur):
	if (cur[1] != 0):
		ss = s[cur[0]]
		s[cur[0]] = ss[:cur[1]]
	return cur

def cmd_dd(s, cur):
	if (cur[0] >= 0):
		s.pop(cur[0])
		if (cur[0] == len(s)):
			cur = (cur[0] - 1, 0)
		else:
			cur = (cur[0], 0)
	return cur
def cmd_ddp(s, cur):
	if (cur[0] < len(s) - 1):
		s[cur[0]], s[cur[0] + 1] = s[cur[0] + 1], s[cur[0]]
		cur = (cur[0] + 1, cur[1])
	return cur
def cmd_n(s, cur, word):
	cur = (cur[0], s[cur[0]].find(word, cur[1]))
	return cur
def printing(s, cur) :
	for i in range(len(s)):
		if i == cur[0]:
			print(s[i][:cur[1]] + colored('^', 'red') + s[i][cur[1]:])
		else:
			print(s[i])
	print("-------------")