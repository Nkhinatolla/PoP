import LinkedList as LL

cursor = [1, 5]

file = open("input_3.txt", "r");

start_node = LL.create_LL(file)
file.close()

last = LL.find_last_node(start_node)

