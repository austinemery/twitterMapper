from twython import Twython, TwythonError
import webbrowser
# Requires Authentication as of Twitter API v1.1

APP_KEY = 'yHroQigAN9DRz9NGFxQilA1uk'
APP_SECRET = 'QffsFUDwzI4RFerNBTWCJ0gBH5uvq5TCKrJW2HcQzZzKoHLito'
OAUTH_TOKEN =  '981718285379977216-BcJhxpzS5HEwcXf8D6QWWTliiDmFv6d'
OAUTH_TOKEN_SECRET = 'ERS7aq8DYOkoh0JsG5JNvE1ulAo3msTtuq2UQ8sc4DzXR'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

location = None

fileOut = open('userLocations.txt','w')

#while location == None:
try:
    search_results = twitter.search(q = 'Reno', count = 200)

except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    
    if tweet['geo'] != None:
		print tweet['coordinates']['coordinates'], '\n'
		location = tweet['place']

		fileOut.write(tweet['user'], " : ", tweet['coordinates']['coordinates'], '\n')

fileOut.close()

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