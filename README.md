Do you use Twitter? If so, then you must come across some of the bots that like, retweet, follow, or even reply to your tweets. But have you ever wondered how they are made? Well, it's easy as filling water in a bottle. Haha! It's really not rocket science. So, let's get started and make a bot.    

![image](https://media.makeameme.org/created/bots-bots-9c4m68.jpg)

In Python, the twitter bot is just a few lines of code, less than 30.   

## Prerequisites for making one (Bot)  

    - tweepy module in Python.
    - A twitter account, which you want to make a bot.
    - Twitter developer account.

## Applying to the twitter developer account
To apply for the developer account on twitter, follow these steps:  
- Go to this [link](https://developer.twitter.com/).  
     You will get this kind of website after you visit the mentioned link.
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/xoyshpkdtzqvutizf4wq.png)

Make sure you've logged in to your Twitter account on which you want to make a bot.  
Here, I'm using my new account **BashWoman** to make a bot, which will like, and retweet the hashtag #python3.    
 - Click on apply, after doing that this type of screen will show up.  
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ob30ksku8512ce95hnrb.png)
Select, **apply for a developer account.**  
- After this, you will get a number of options, why you want to apply for the developer account, here we are making a bot, so I will select **Making a bot**.  
   
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/zbdvc49baifrm3llzil3.png)  

- Now, on the next page, you have to fill some details. Do that.  
  
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/vs7uj15z5fueu6at9bp6.png)  

- Twitter will ask you some questions related to how you would use this account and the twitter data. We are just making this bot to like and retweet the posts so, select that only.  
    
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/bx796t9u3sp55ay0ywrg.png)  

And  
  
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/97e9hcfp5h2zv7os6isx.png)  

Else select no, just to keep it simple.
Enter all the details you'd do with this bot.  
  
- After filling all the details, you'll get an agreement page. Just accept all the terms and conditions. And then click on **Submit application**.  
  
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/ops5v8yy58ont94ap2ub.png)  

- You will get a confirmation mail. Once you confirm that, a new window will open like this.  

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/wd6iepn5j3f4zq01h5tb.png)  

Click **Get keys**.
- After this, what we wanted by this developer account is the keys. Save them somewhere, you'll need them soon.  

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/1hx4apw6bxo152vzrss2.png)  

## Let's Code and understand it

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6hwd9o5kt84jyjbiemos.png)  

You see there are no more than 30 lines in Python. Let's understand each and every line.  

```
import tweepy
import time
```
To communicate with Twitter API, we need some module, here we are using **tweepy**. You can install it easily.  
```
pip install tweepy
```

Once you install the module, write some more code.

```
# Authenticate to Twitter
CONSUMER_KEY = '<your-consumer-or-API-key-goes-here>'
CONSUMER_SECRET = '<your-consumer-or-API-secret-goes-here>'
ACCESS_KEY = '<your-access-key-goes-here>'
ACESS_SECRET = '<your-access-secret-goes-here>'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACESS_SECRET)
```

This is used to authenticate your Twitter account. Remember these keys are of your account, don't share them to anyone, else they can access your data. That's why I have made some variables in which I will store the keys.  

These keys will be found in your developer account, which you've saved a time ago.  

**auth** variable is created to authenticate the account, Twitter uses OAuth to do this.  
And, after that, we will set the tokens.  

```
# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
```  

This class provides a wrapper for the API as provided by Twitter. If you stuck somewhere, you can always refer to the [tweepy documentation](http://docs.tweepy.org/en/latest/).  

```
user = api.me()
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
```
Finally, we will tell the program to look for the keyword **#python3** in a tweet and the number of tweets that will be processed once in a day. If you want to like, you can use **tweepy.favorite()** , and for retweet **tweepy.retweet()**. 
The reason, I'm using sleep is, twitter has some guidelines, you must follow otherwise, your account will be restricted. There is a limit for liking the number of tweets. If it gives some error, we can use **tweepy.TweepError** so that we know, what went wrong.  

Now, it's time for the deployment. You can use any platform, I have used [Render](https://render.com/).  
After creating an account on this, create a cron job, you can schedule the time, I prefer about 10 to 15 mins. It means your bot will run every 10 to 15 mins so that it won't violate the Twitter guidelines and your account will be safe and not get restricted. 

Here's my bot.  

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/yv731bysoy4jscv8cz5w.png)  

It's time to build your own bot. 
All the best. 
