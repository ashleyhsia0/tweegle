"""Functions to make JSONs for AngularJS"""

import json


def jsonify_tweets(tweets):
    """Return Tweepy tweet objects as JSON."""

    tweets_list = []

    for tweet in tweets:
        tweet_dict = {
            "userName": tweet.user.name,
            "userHandle": tweet.user.screen_name,
            "userProfileImg": tweet.user.profile_image_url,
            "tweetId": tweet.id_str,
            "tweetContent": tweet.text,
            "tweetDate": (tweet.created_at).isoformat(),  # Create serialized version for datetime object
            "tweetRetweets": tweet.retweet_count,
            "tweetFavorites": tweet.favorite_count
        }

        tweets_list.append(tweet_dict)

    return json.dumps(tweets_list)
