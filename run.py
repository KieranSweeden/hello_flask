import os
# flask framework in lower caps, flask class in uppercase as it's a class, render_template is function
from flask import Flask, render_template

# Create an instance of flask, storing it in variable named app
# 1st parameter of Flask class, is the name of the application's
# module, our package. Since we're only using 1 module, we can use the built-in
# Python variable __name__.
# Flask needs this so that it knows where to look for templates & static files
app = Flask(__name__)


# We're then using the app.route decorator, using the @ symbol, which is also
# called pie-notation. This wraps the function underneath.
# As we try to browse to the root directory, as indicated by the "/" parameter, Flask
# then triggers the index function underneath and return the "Hello, World" text.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

# __main__ is the name of the default module in Python.
# This is the first one that we run, however if this has not been imported(which it won't be),
# then it's going to be run directly
if __name__ == "__main__":
    # We then want to run our app using the arguments that we've passed inside of this app.run statement.
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # WE SHOULD NOT HAVE DEBUG=TRUE IN A PRODUCTION APPLICATION, it has security flaws
        debug=True
    )