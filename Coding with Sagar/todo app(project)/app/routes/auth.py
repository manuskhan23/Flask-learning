from flask import flash, Flask, Blueprint, render_template, request, redirect, url_for, session, jsonify
import uuid

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":        
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        
        if len(password) < 6:
            flash("Password must be at least 6 characters long", "danger")
            return redirect(url_for("auth.register"))
        
        from app.models import User
        from app import db

        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash("Username already exists", "danger")
            return redirect(url_for("auth.register"))

        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successful! Please Login", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("auth/signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        if len(password) < 6:
            flash("Password must be at least 6 characters long", "danger")
            if is_ajax:
                return jsonify({"success": False, "message": "Password must be at least 6 characters long"}), 400
            return redirect(url_for("auth.login"))
        
        from app.models import User
        user = User.query.filter_by(username=username, password=password).first()
        
        if user:
            session["user"] = username
            user_id = str(uuid.uuid4())
            session["user_id"] = user_id
            flash("Login Successful", "success")
            
            # Return JSON response for AJAX request
            if is_ajax:
                return jsonify({"success": True, "user_id": user_id, "username": username})
            
            return redirect(url_for("task.view_tasks"))
        else:
            flash("Invalid Credentials", "danger")
            if is_ajax:
                return jsonify({"success": False, "message": "Invalid Credentials"}), 401
    
    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("user_id", None)
    flash("Logout Successful", "info")
    
    # Return JSON response for AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({"success": True})
    
    return redirect(url_for("auth.login"))
