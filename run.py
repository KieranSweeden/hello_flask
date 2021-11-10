import os
import json
# flask framework in lower caps, flask class in uppercase as it's a class, render_template is function
from flask import Flask, render_template, request, flash
# request library is going to finding out what method we used and will contain that form object that's been posted
# flash library allows us to display messages with short timeouts, essentially being a "flashed message" to the user
if os.path.exists("env.py"):
    import env

# Create an instance of flask, storing it in variable named app
# 1st parameter of Flask class, is the name of the application's
# module, our package. Since we're only using 1 module, we can use the built-in
# Python variable __name__.
# Flask needs this so that it knows where to look for templates & static files
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


# We're then using the app.route decorator, using the @ symbol, which is also
# called pie-notation. This wraps the function underneath.
# As we try to browse to the root directory, as indicated by the "/" parameter, Flask
# then triggers the index function underneath and return the "Hello, World" text.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []

    with open("data/company.json", "r") as json_data: # Open the company.json file as read only ("r") and store as json_data variable
        data = json.load(json_data)

    return render_template("about.html", page_title="About", company=data)

@app.route("/about/<member_name>") # Angle brackets will pass in data from URL path into the view below, it's given a parameter name of member_name
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member) # 1st member is variable name being passed to html, 2nd member is object initialised on line 34


@app.route("/contact", methods=["GET", "POST"]) # Tells flask this particular view should accept both get and post methods, as it's only get by default
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name"))) # name is injected within the {} of the flash message by the format method


        # print(request.form.get("name")) # Access form data given using dot notation and get method as it returns an immutable dictionary - throws None value if nothing is there
        # print(request.form["email"]) # Access form data given using square brackets - throws exception if nothing is there
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

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