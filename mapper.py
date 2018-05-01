from twython import Twython, TwythonError
import webbrowser
# Requires Authentication as of Twitter API v1.1

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

###########################################################################################
#
# Name: listToFormattedStringList(coorArray)
# Purpose: To convert each element inside coorArray to a string and to format it as 'aNumber%2CaNumer'
#
# Notes:   
#
###########################################################################################

def listToFormattedStringList(coorArray):
	stringCoor = []

	for e in coorArray:
		stringCoor.append(str(e))

	stringCoor = [s.replace(',', '%2C').replace(' ', '') for s in stringCoor]

	return stringCoor

def main():

	###############
	# API Relevant 
	###############
	APP_KEY = 'yHroQigAN9DRz9NGFxQilA1uk'
	APP_SECRET = 'QffsFUDwzI4RFerNBTWCJ0gBH5uvq5TCKrJW2HcQzZzKoHLito'
	OAUTH_TOKEN =  '981718285379977216-BcJhxpzS5HEwcXf8D6QWWTliiDmFv6d'
	OAUTH_TOKEN_SECRET = 'ERS7aq8DYOkoh0JsG5JNvE1ulAo3msTtuq2UQ8sc4DzXR'
	twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	##############
	# Variables
	##############
	defaultUser = "tmj_NV_EDU"
	location = None
	chosenUser = None
	coorArray = []
	

	#############
	# User Interaction
	#############
	searchLocation = input("Where would you like to search? | Ex:\"san franscisco\" | ")
	print searchLocation

	fileOut = open('userLocations.txt','w')

	#############
	# Search for a user in that area.
	#############
	#while location == None:
	try:
	    search_results = twitter.search(q = searchLocation, count = 150)

	except TwythonError as e:
	    print e

	for tweet in search_results['statuses']:
	    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
	    
	    if tweet['geo'] != None:
			print tweet['coordinates']['coordinates'], '\n'
			location = tweet['coordinates']['coordinates']

			#fileOut.write(tweet['user']['screen_name'].encode('utf-8'))
			#fileOut.write(" : " + ' '.join(str(e) for e in location) + '\n')

			chosenUser = tweet['user']['screen_name'].encode('utf-8')

	#############
	# Determine if a user was found, if not, set a default user
	#############
	if chosenUser == None:
		chosenUser = defaultUser
		print "No users for your search were found. A default user has been selected.\n"

	print "The chosenUser is " , chosenUser , '\n'
	print "\n\n"

	#############
	# Search the user for information
	#############
	try:
	    search_results = twitter.search(q = chosenUser, count = 150)

	except TwythonError as e:
	    print e

	for tweet in search_results['statuses']:
	    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
	    
	    if tweet['geo'] != None:
			print tweet['coordinates']['coordinates'], '\n'
			location = tweet['coordinates']['coordinates']
			coorArray.append(location)
			
			fileOut.write(tweet['user']['screen_name'].encode('utf-8'))
			fileOut.write(" : " + ' '.join(str(e) for e in location) + '\n')

	coorArray = listToFormattedStringList(coorArray)

	url = urlBuilder(coorArray)

	webbrowser.open(url, new=1, autoraise=True)

	fileOut.close()

	print ', '.join(map(str, location))

	return

if __name__ == "__main__":
	main()