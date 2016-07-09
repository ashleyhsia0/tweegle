from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

import os
import tweepy

import operator

# Set up Tweepy (Twitter API library)
auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"],
                           os.environ["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN_KEY"],
                      os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

twitter_api = tweepy.API(auth)

# Set up Flask web app
app = Flask(__name__)
app.secret_key = "ABC123"

# Raise an error for undefined variable in Jinja2, rather than failing silently
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage with search engine"""

    return render_template("homepage.html")


@app.route("/search", methods=["GET"])
def show_login():
    """Show search results"""

    user_query = request.args.get("q")

    tweet_search_results = twitter_api.search(user_query)
    user_search_results = twitter_api.search_users(user_query)

    hashtags = {}

    for tweet in tweet_search_results:
        for item in tweet.entities['hashtags']:
            hashtag = item['text']
            hashtags[hashtag] = hashtags.get(hashtag, 0) + 1

    # Sort hashtags based on count in ascending order
    sorted_hashtags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)

    return render_template("search_results.html",
                           tweet_search_results=tweet_search_results,
                           user_search_results=user_search_results,
                           sorted_hashtags=sorted_hashtags)


if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run()
