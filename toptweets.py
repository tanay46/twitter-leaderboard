import simplejson
import urllib
username = "someusername"
tweets = {}
ids = {}
i = 1
numberoftoptweets = 10
# get all tweets and their retweet counts
while(1):
	url = "https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=false&screen_name=" + username + "&count=200&page=" + str(i)
	page = simplejson.load(urllib.urlopen(url))
	if not page:
		break
	for s in page:
		tweets[s['text']] = s['retweet_count']
		ids[s['text']] = s['id']
	i+=1	
# sort the tweets by retweet count
for k in sorted(tweets, key=tweets.get, reverse=True)[:numberoftoptweets]:
	print k,"=>", tweets[k]
