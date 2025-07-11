import tweepy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Twitter Bearer Token from environment variables
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Initialize Tweepy client
if not TWITTER_BEARER_TOKEN:
    print("Twitter Bearer Token is missing. Please set it in the .env file.")
else:
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

# Function to fetch tweets by city
def fetch_tweets_by_city(city):
    if not TWITTER_BEARER_TOKEN:
        return []  # Exit if the Bearer Token is missing

    query = f"({city} lang:en) OR ({city} lang:hi) -is:retweet" 
    tweets = client.search_recent_tweets(query=query, max_results=10)
    
    # Get tweet texts
    tweet_list = [tweet.text for tweet in tweets.data] if tweets.data else []
    
    return tweet_list
