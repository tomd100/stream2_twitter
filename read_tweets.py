import json

results = []

tweets_file = open('tweet_mining.json', 'r')
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue

hashtags_set = set()

for tweet in results:
    hashtags = tweet['entities']['hashtags']
    if not hashtags == []:
        # print(hashtags)
        for hashtag in hashtags:
            hashtags_set.add(hashtag['text'])
            
hashtags_list = list(hashtags_set)

print(hashtags_list)
            
            
            