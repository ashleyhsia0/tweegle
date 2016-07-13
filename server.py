from jinja2 import StrictUndefined

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from twitter_api_call import fetch_results, fetch_hashtags

# Set up Flask web app
app = Flask(__name__)
app.secret_key = "ABC123"

# Raise an error for undefined variable in Jinja2, rather than failing silently
app.jinja_env.undefined = StrictUndefined


@app.template_filter()
def datetimefilter(value, format='%b %d'):
    """Convert a datetime to a different format so it can be accessible in Jinja."""

    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter


@app.route('/')
def index():
    """Homepage with search engine"""

    return render_template("homepage.html")


@app.route("/search", methods=["GET"])
def search():
    """Show search results"""

    user_query = request.args.get("q")

    # Get results for tweets and users from Twitter based on user query
    tweet_search_results, user_search_results = fetch_results(user_query)

    # Get hashtags for tweets retrieved
    sorted_hashtags = fetch_hashtags(tweet_search_results)

    return render_template("search_results.html",
                           tweet_search_results=tweet_search_results,
                           user_search_results=user_search_results,
                           sorted_hashtags=sorted_hashtags)


if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run(threaded=True)
