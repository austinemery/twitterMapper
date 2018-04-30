from twython import Twython, TwythonError

# These long things are needed, do NOT change them

APP_KEY = 'yHroQigAN9DRz9NGFxQilA1uk'
APP_SECRET = 'QffsFUDwzI4RFerNBTWCJ0gBH5uvq5TCKrJW2HcQzZzKoHLito'
OAUTH_TOKEN =  '981718285379977216-BcJhxpzS5HEwcXf8D6QWWTliiDmFv6d'
OAUTH_TOKEN_SECRET = 'ERS7aq8DYOkoh0JsG5JNvE1ulAo3msTtuq2UQ8sc4DzXR'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

location = None

searchLocation = input("Where would you like to search?")

fileOut = open('userLocations.txt','w')

#while location == None:
try:
    search_results = twitter.search(q = searchLocation, count = 50)

except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'])
    
    if tweet['geo'] != None:
		print tweet['coordinates']['coordinates'], '\n'
		location = tweet['coordinates']['coordinates']

		fileOut.write(tweet['user']['screen_name'].encode('utf-8'))
		fileOut.write(" : " + ' '.join(str(e) for e in location) + '\n')

fileOut.close()