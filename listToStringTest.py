coordinates = [[33, 22], [44, 66], [77, 88]]

stringCoor = []

for e in coordinates:
	stringCoor.append(str(e))

for test in stringCoor:
	print test


stringCoor = [s.replace(',', '%2C').replace(' ', '') for s in stringCoor]

for test in stringCoor:
	print test