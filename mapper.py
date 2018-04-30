from twython import Twython, TwythonError

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