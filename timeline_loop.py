from tweepy import Stream
from tweepy.streaming import StreamListener
from auth import get_auth

keyword_list=['brexit']
limit = 20

class MyStreamListener(StreamListener):
    
    def __init__(self):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        
    def on_data(self, data):
        if self.num_tweets <= limit:
            self.num_tweets += 1
            try:
                with open('tweet_mining.json', 'a') as tweet_file:
                    tweet_file.write(data)
                    return True
            except BaseException as e:
                print("Failed on_data: {0}".format(e))
            return True
        else:
            return False
        
        def on_error(self, status):
            print(status)
            return True

auth = get_auth()

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track = keyword_list)
