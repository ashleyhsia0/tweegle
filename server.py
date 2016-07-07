from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension

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

    return render_template("search_results.html")


if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)
    app.run()