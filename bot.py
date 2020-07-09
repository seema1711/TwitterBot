import tweepy
import time

# Authenticate to Twitter

CONSUMER_KEY = '1gCJf1tHvCBOspbEk0K80G7cU'
CONSUMER_SECRET = 'Tk65NYp79UHHGxXbcJWnWKF47OZwjBJHVcNjpJlwUw6S5WOdFY'
ACCESS_KEY = '1281248101106249728-Qzmy95X1pBrtJEB7tE78DoOq7F29NU'
ACESS_SECRET = '3CNS3xrYspXaCSGav8Mdj9E1YuwLiXHSsGwCKIPUG05kM'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
# for follower in tweepy.Cursor(api.followers).items():
#    print(follower.name)
search = '#python3'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweet Liked')
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break