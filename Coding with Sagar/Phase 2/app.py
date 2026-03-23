from flask import Flask,render_template

app=Flask(__name__ )

# @app.route("/")
# def Student():
#     return render_template(
#                     "profile.html",
#                     name="Anus",
#                     isTopper=True,
#                     subjects=["english","urdu","maths"]
#                     )

@app.route("/")
def home():
    return render_template("jinja2-home.html")

@app.route("/about")
def about():
    return render_template("jinja2-about.html")