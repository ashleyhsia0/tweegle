"""Functions to retrieve information from Twitter API"""

import os
import tweepy
import operator

# Set up Tweepy (Twitter API library)
auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"],
                           os.environ["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN_KEY"],
                      os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

twitter_api = tweepy.API(auth)


def fetch_results(user_query):
    """
    Fetch search results from Tweepy/Twitter API based on user query.

    Return 200 tweets (Twitter default is set to 20).
    Return 100 users (Twitter default is set to 15).
    """

    tweet_search_results = [tweet for tweet in tweepy.Cursor(twitter_api.search, q=user_query).items(200)]
    user_search_results = [user for user in tweepy.Cursor(twitter_api.search_users, q=user_query).items(100)]

    return tweet_search_results, user_search_results


def fetch_hashtags(tweets):
    """Get all hashtags for tweets, along with the count, sorted in descending order based on the count."""

    hashtags = {}

    for tweet in tweets:
        for item in tweet.entities['hashtags']:
            hashtag = item['text']
            hashtags[hashtag] = hashtags.get(hashtag, 0) + 1

    # Sort hashtags based on count in descending order
    sorted_hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_hashtags
