location = None
coorArray = []

while location != "end":
	location = input('Enter Coordinate: ')
	if  coorArray.count(location) == 0:
		coorArray.append(location)
	print(coorArray)
