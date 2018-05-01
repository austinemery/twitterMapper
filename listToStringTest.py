
###########################################################################################
#
# Name: listToFormattedStringList(coorArray)
# Purpose: To convert each element inside coorArray to a string and to format it as 'aNumber%2CaNumer'
#
# Notes:
#		1. The   
#
###########################################################################################

def listToFormattedStringList(coorArray):

	stringCoor = []

	for e in coorArray:
		stringCoor.append(str(e))

	stringCoor = [s.replace(',', '%2C').replace(' ', '').replace('[', '').replace(']', '') for s in stringCoor]

	return stringCoor

coordinates = [[1, 2], [2, 3], [3, 4]]

blah = listToFormattedStringList(coordinates)

for e in blah:
	print e