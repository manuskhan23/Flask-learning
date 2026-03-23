from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")

    valid_users={
        "admin":"123",
        "anus":"anus123",
        "huzaifa":"huzaifa123",
        "nawab":"nawab123"
    }

    if username in valid_users and password in valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return "Invalid Credential"