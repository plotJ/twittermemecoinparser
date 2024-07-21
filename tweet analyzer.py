import tweepy
import pandas as pd
from textblob import TextBlob

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# ID of the Twitter list
list_id = "1556982891778809857"

# Function to get tweets from the list
def get_list_tweets(list_id, max_tweets=100):
    tweets = []
    for tweet in tweepy.Cursor(api.list_timeline, list_id=list_id).items(max_tweets):
        tweets.append(tweet)
    return tweets

# Function to analyze sentiment of a tweet
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet.text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Get tweets from the list
tweets = get_list_tweets(list_id)

# Analyze tweets
analyzed_tweets = []
for tweet in tweets:
    analyzed_tweets.append({
        'text': tweet.text,
        'user': tweet.user.screen_name,
        'created_at': tweet.created_at,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count,
        'sentiment': analyze_sentiment(tweet)
    })

# Convert to DataFrame for easy analysis
df = pd.DataFrame(analyzed_tweets)

# Print basic statistics
print(df['sentiment'].value_counts())
print(df.groupby('user')['sentiment'].value_counts())