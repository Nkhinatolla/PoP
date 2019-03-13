Dict = {"Albert":"March 14, 1879", "Stephen":"January 8, 1942", "Isaac":"January 4, 1643"}
name = input()
if Dict.get(name) != None:
	print(Dict[name])
else:
	print("There is no " + name + " in our dictionary")
