INFO = 0
NEXT_PTR = 1
PREV_PTR = 2
def create_node(data):
	return [data, None, None]

def find_last_node(start):
	current_ptr = start
	while True:
		print(current_ptr[INFO])
		if current_ptr[NEXT_PTR] != None:
			current_ptr = current_ptr[NEXT_PTR]
		else:
			return(current_ptr)
def create_LL(file):
	l = []
	for line in file:
		line = line[:-1]
		l.append(create_node(line))

	for i in range(len(l) - 1):
		l[i][NEXT_PTR] = l[i + 1]
		if (i != 0):
			l[i][PREV_PTR] = l[i - 1]
	return l[0]