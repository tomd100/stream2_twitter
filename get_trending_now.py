import json
import tweepy


from auth import get_api

api = get_api()

def get_my_timeline(count):
    return tweepy.Cursor(api.home_timeline).items(count)


def get_my_search(query, count):
    return tweepy.Cursor(api.search, q=query).items(count)

# for status in get_my_timeline(1):
#     print(status)

tweets = get_my_search("Storm Brian", 10)

for tweet in tweets:
    tweet = tweet._json
    tweet_text = json.dumps(tweet) 
    with open("brian.text", "+w") as outfile:
        outfile.write(tweet_text)



# print(tweets)
# tweets_text = json.dumps(tweets[0])

# for tweet in tweets:
#     print(json.dumps(tweet))
#     # with open("brian.json", "+w"):
        

# tweets_text = json.dumps(tweets)
