Dict = {0:["Astana"], 1:["Pavlodar","Karaganda"], 2:["Oskemen"], 3:["Atyrau", "Aktay", "Oral"], 4:["Almaty"]}
source = input("Input source: ")
destination = input("Input destination: ")
def rec(ind, ans, indexOfSource, indexOfDestination):
	if not (ind in Dict): 
		return
	if ind == indexOfSource:
		rec(ind + 1, source + ",", indexOfSource, indexOfDestination)
		return
	if ind == indexOfDestination:
		ans += destination
		print(ans)
		return
	for city in Dict[ind]:
		rec(ind + 1, ans + city + ",", indexOfSource, indexOfDestination)
indexOfDestination = -1
indexOfSource = -1
for index in Dict:
	for city in Dict[index]:
		if (city == destination):
			indexOfDestination = index
		if (city == source):
			indexOfSource = index
if indexOfDestination != -1 and indexOfSource != -1:
	rec(indexOfSource, "", indexOfSource, indexOfDestination)
else:
	print("There is no city called " + destination)