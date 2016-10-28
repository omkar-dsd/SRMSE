# explained on http://socialmedia-class.org/twittertutorial.html

try:
	import json

except ImportError:
	import simplejson as json


from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


config={'ACCESS_TOKEN':'2770722877-Z7GqeEB5APHMhBHalZjcR42dQhRJHY0TKj80Szv','ACEESS_SECRET':'5WrsjqYaCB6zLV08LUiAP94HZ5EuviDu2vj3joIwdByfL','CONSUMER_KEY':'03ycPyPiPWBrB17GGq3LiWxiE','CONSUMER_SECRET':'w4sTeDYmdL8OEVQYpVrICpgsV06CZGwebFSyOrNJL6McE0ri9S'}
#Authentication keys from apps.twitter.com

#ACCESS_TOKEN = '2770722877-Z7GqeEB5APHMhBHalZjcR42dQhRJHY0TKj80Szv'
#ACEESS_SECRET = '5WrsjqYaCB6zLV08LUiAP94HZ5EuviDu2vj3joIwdByfL'
#CONSUMER_KEY = '03ycPyPiPWBrB17GGq3LiWxiE'
#CONSUMER_SECRET = 'w4sTeDYmdL8OEVQYpVrICpgsV06CZGwebFSyOrNJL6McE0ri9S'

oauth = OAuth(config['ACCESS_TOKEN'], config['ACEESS_SECRET'], config['CONSUMER_KEY'], config['CONSUMER_SECRET'])

#Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
# iterator = twitter_stream.statuses.sample()


#Filter tweets containing term Google
iterator = twitter_stream.statuses.filter(track = 'Google', language = 'en')

#Limiting number of tweets, not mandatory
tweet_count = 100
for tweet in iterator:
	tweet_count -=1

	
	print json.dumps(tweet, indent = 4)

	if tweet_count <= 0:
		break


    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)



