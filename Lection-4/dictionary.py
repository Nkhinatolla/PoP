thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1992 2000",
  1: 4
}
print(thisdict)

x = thisdict[1]
print(x)

for x in thisdict:
  print(x, end = " ")      #printing keys: brand model year
print()
for x in thisdict:
  	print(thisdict[x], end = " ")    #printing value: 


Dict = {"Albert":"March 14, 1879", "Stephen":"January 8, 1942", "Isaac":"January 4, 1643"}
name = input("Enter name: ")
print(Dict.get(name))
print(len(Dict))
Dict.pop("Albert")
Dict.update({"Stephen" : True})
print("----------")
print(list(Dict.values()))
D = {2 : False}
D = D.fromkeys([2, 3, 4, 4], 1)
print(D)
print(D.popitem())
print(D)	
print("------")
D.setdefault(5)
print(D)
T = {"x": 1}
T.update({"x": T["x"] + 1})
print(T)

# if Dict.get(name) != None:
# 	print(Dict[name])
# else:
# 	print("There is no " + name + " in our dictionary")
