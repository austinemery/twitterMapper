from twython import Twython, TwythonError
import webbrowser
# Requires Authentication as of Twitter API v1.1


APP_KEY = 'yHroQigAN9DRz9NGFxQilA1uk'
APP_SECRET = 'QffsFUDwzI4RFerNBTWCJ0gBH5uvq5TCKrJW2HcQzZzKoHLito'
OAUTH_TOKEN =  '981718285379977216-BcJhxpzS5HEwcXf8D6QWWTliiDmFv6d'
OAUTH_TOKEN_SECRET = 'ERS7aq8DYOkoh0JsG5JNvE1ulAo3msTtuq2UQ8sc4DzXR'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
defaultUser = "tmj_NV_EDU"
location = None
chosenUser = None
coorArray = []
searchLocation = input("Where would you like to search? | Ex:\"san franscisco\" | ")
print searchLocation

fileOut = open('userLocations.txt','w')

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


if chosenUser == None:
	chosenUser = defaultUser
	print "No users for your search were found. A default user has been selected.\n"

print "The chosenUser is " , chosenUser , '\n'
print "\n\n"


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


fileOut.close()

print ', '.join(map(str, location))

'''
URL builder

urlStart = "https://www.google.com/maps/dir/?api=1&parameters"
urlOrigin = "&origin=" + coorArray[0] + "%2C" + coorArray[1]

#handle the waypoints

index = 2
urlWaypoints = "&waypoints="
for index < (coorArray.size() - 2)
	if index != (coorArray.size() - 2):
		urlWaypoint += coorArray[index] + "%2C"
		index += 1
		urlWaypoint += coorArray[index] + "%7C"
	elif:
		urlWaypoint += coorArray[index] + "%2C" + coorArray[index+1]


urlDestination = "&destination=" + coorArray[coorArray.size()-1] + "%2C" + coorArray[coorArray.size()]
urlMode = "&travelmode=driving"

urlComplete = urlStart + urlOrigin + urlWaypoint + urlDestination + urlMode

print urlComplete

webbrowser.open(urlComplete, new=1, autoraise=True)

'''


#https://www.google.com/maps/dir/?api=1&origin=-33.868882%2C151.197360&waypoints=-33.871420%2C151.196168%7C-33.875117%2C151.199159&destination=-33.872256%2C151.204530&travelmode=driving
