# explained on http://socialmedia-class.org/twittertutorial.html
#The Twitter Search API searches against a sampling of recent Tweets published in the past 7 days.


try:
	import json

except ImportError:
	import simplejson as json


from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream


#Authentication keys from apps.twitter.com
config={'ACCESS_TOKEN':'2770722877-Z7GqeEB5APHMhBHalZjcR42dQhRJHY0TKj80Szv','ACEESS_SECRET':'5WrsjqYaCB6zLV08LUiAP94HZ5EuviDu2vj3joIwdByfL','CONSUMER_KEY':'03ycPyPiPWBrB17GGq3LiWxiE','CONSUMER_SECRET':'w4sTeDYmdL8OEVQYpVrICpgsV06CZGwebFSyOrNJL6McE0ri9S'}
#Authentication keys from apps.twitter.com

#ACCESS_TOKEN = '2770722877-Z7GqeEB5APHMhBHalZjcR42dQhRJHY0TKj80Szv'
#ACEESS_SECRET = '5WrsjqYaCB6zLV08LUiAP94HZ5EuviDu2vj3joIwdByfL'
#CONSUMER_KEY = '03ycPyPiPWBrB17GGq3LiWxiE'
#CONSUMER_SECRET = 'w4sTeDYmdL8OEVQYpVrICpgsV06CZGwebFSyOrNJL6McE0ri9S'

oauth = OAuth(config['ACCESS_TOKEN'], config['ACEESS_SECRET'], config['CONSUMER_KEY'], config['CONSUMER_SECRET'])


# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)
            
world_trends = twitter.trends.available(_woeid=1)

for i in world_trends:
	print i

