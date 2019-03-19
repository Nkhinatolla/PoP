l = [2, 24, 34, 3434, 32, 33, 2, 2]
l.append(2)
print(l.count(2))
print(l.count(-1))
l.insert(2, True)
l.insert(2, 0)
print(l)
l.sort()
print(l)
r = ["String", "Ab", "sds", "Abb"]
r.sort()
print(r)
#r.pop()
#print(r)
# r.remove("Ab")
print(r)
r.extend([3, 2])
print(r)
r.reverse()
print(r)
if "Ab" in r:
	print(r.index("Ab"))

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count("orange")	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop(3)	Removes the element at the specified position
# remove("orange")	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()
