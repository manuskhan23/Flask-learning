from flask import Flask,render_template,request,redirect,url_for,flash
from form import RegistrationForm
app=Flask(__name__)
app.secret_key="ytfhc"

# @app.route("/feedback",methods=["GET","POST"])
# def feedback():
#     if request.method=="POST":
#         name=request.form.get("username")
#         msg=request.form.get("msg")

#         return render_template("thanks.html", user=name , fb=msg)
    
#     return render_template("feedback.html")

# ----------------------------------------------------
# flash messages (flash , get_flashed_message) 
# ----------------------------------------------------

# def:any message that show only one time like after shoping we see "Thank you for purshasing"

# @app.route("/",methods=["GET","POST"])
# def form():
#     if request.method=="POST":
#         name=request.form.get("name")
#         if not name:
#             flash("Name section should not be empty,")
#             return redirect(url_for("form"))
#         flash(f"Thanks {{user}} for Your Form Submission!")
#         return render_template("thanks.html")           
#     return render_template("form.html")
    
# @app.route("/thanks")
# def thanks():
#     return render_template("thanks.html")

@app.route("/",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        name=form.username.data
        email=form.email.data
        
        # FIX: added category
        flash(f"Welcome, {name}! You registered successfully.", "message")
        
        return redirect(url_for("success"))
    return render_template("register.html",form=form)

@app.route("/success")
def success():
    return render_template("success.html")


# -----------------------------------
# CSRF=Cross Site Request Forgery
# -----------------------------------