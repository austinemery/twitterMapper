'''
-33.868882, 151.197360
-33.871420, 151.196168
-33.875117,151.199159
-33.872256, 151.204530

coorArray = ["-33.868882%2C151.197360", "-33.871420%2C151.196168" , "-33.875117%2C151.199159" , "-33.872256%2C151.204530"]
'''

###########################################################################################
#
# Name: urlBuilder( coorArray )
# Purpose: To construct the URL that will map the twitter user based on their locations
# Cases:
# 		1. There is only one location in the array.
#			In this case the map will open with only one point on the map, with the one
#			location being the origin and the destination.
#		2. There are two locations in the array.
#			In this case the map will open with the first point being the origin and
#			the last point being the destination.
#		3. The are more than two locations in the array.
#			In this case the map will open with the first point being the origin,
#			the last point being the destination, and all other points being Waypoints.
#
#
# Notes:
#		1. Amount of Waypoints allowed:
#			-3 if on mobile
#			-9 otherwise
#			Therefore we will assume that the attack is being run from a computer
#			and will only include 11 location points in an array.  
#
###########################################################################################

import webbrowser

def urlBuilder( coorArray ):
	urlStart = "https://www.google.com/maps/dir/?api=1&parameters"
	urlOrigin = "&origin=" + coorArray[0]

	#handle the waypoints
	urlWaypoints = "&waypoints="
	for index in range(len(coorArray)):
		if index == 0 or index == (len(coorArray)-1):
			continue
		elif index != (len(coorArray)  - 2):
			urlWaypoints += coorArray[index] 
			urlWaypoints += "%7C"
		else:
			urlWaypoints += coorArray[index]


	urlDestination = "&destination=" + coorArray[index]

	urlMode = "&travelmode=driving"

	urlComplete = urlStart + urlOrigin + urlWaypoints + urlDestination + urlMode

	return urlComplete

#webbrowser.open(urlComplete, new=1, autoraise=True)