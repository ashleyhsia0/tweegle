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
            "id": tweet.id_str,
            "text": tweet.text,
            "date": (tweet.created_at).isoformat(),  # Create serialized version for datetime object
            "numRetweets": tweet.retweet_count,
            "numFavorites": tweet.favorite_count
        }

        tweets_list.append(tweet_dict)

    return json.dumps(tweets_list)


def jsonify_users(users):
    """Return Tweepy user objects as JSON."""

    users_list = []

    for user in users:
        user_dict = {
            "name": user.name,
            "handle": user.screen_name,
            "profileImg": user.profile_image_url,
            "location": user.location,
            "description": user.description,
            "numTweets": user.statuses_count,
            "numFollowers": user.followers_count,
            "numFollowing": user.friends_count
        }

        users_list.append(user_dict)

    return json.dumps(users_list)


def jsonify_hashtags(hashtags):
    """Return list of hashtags as JSON."""

    hashtags_list = []

    for hashtag, count in hashtags:
        hashtag_dict = {
            "name": hashtag,
            "count": count
        }

        hashtags_list.append(hashtag_dict)

    return json.dumps(hashtags_list)
