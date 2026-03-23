from flask import Flask, request, redirect, url_for, session, Response


# ---------------------
# first flask code
# ---------------------

# app=Flask(__name__)

# @app.route("/")

# def home():
#     return "hello user:this is home page"

# @app.route("/about")

# def about():
#     return "hello user:this is about page"

# @app.route("/contact")

# def contact():
#     return "hello user:this is contact page"

# @app.route("/submit",methods=["GET","POST"])
# def submit():
#     if request.method=="POST":
#         return "you sent data!"
#     else:
#         return "you are viewing form only."



# ---------------
# Login (Project 1)
# ---------------

app = Flask(__name__)
app.secret_key="secret"
# login page
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")

        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credential.Please try again!",mimetype="text/plain")
        
    return"""
            <h2>Login Page</h2>
            <form method="POST">
            Username: <input type="text" name="username"/><br/>
            Password: <input type="text" name="password"/><br/>
            <input type="submit" value="Login"/>
            </form>
"""

# Welcome page

@app.route("/")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome, {session["user"]}</h2>
        <a href="{url_for("logout")}">Logout</a>
"""
    return redirect(url_for("login"))


# logout route

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

# ------------------
# Project 1 done
# ------------------