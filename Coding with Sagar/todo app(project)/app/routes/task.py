from flask import Blueprint,render_template,redirect,request,flash,session,url_for
from app.models import Task
from app import db

task_bp=Blueprint("task",__name__)

@task_bp.route("/")
def view_tasks():
    if "user" not in session:
        flash("Please login first","danger")
        return redirect(url_for("auth.login"))
    
    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        flash("User not found","danger")
        return redirect(url_for("auth.login"))
    tasks = Task.query.filter_by(user_id=user.id).all()
    return render_template("todo/todo.html",tasks=tasks)

@task_bp.route("/add",methods=["POST"])
def add_task():
    if "user" not in session:
        flash("Please login first","danger")
        return redirect(url_for("auth.login"))

    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        flash("User not found","danger")
        return redirect(url_for("auth.login"))
    title=request.form.get("title")
    if title:
        new_task=Task(title=title,status="Pending",user_id=user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task Added Successfully","success")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/toggle/<int:task_id>",methods=["POST"])
def toggle_status(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        return redirect(url_for("auth.login"))
    task=Task.query.get(task_id)
    if task and task.user_id==user.id:
        if task.status=="Pending":
            task.status="Working"
        elif task.status=="Working":
            task.status="Done"
        else:
            task.status="Pending"
        db.session.commit()
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/delete/<int:task_id>",methods=["POST"])
def delete_task(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    
    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        return redirect(url_for("auth.login"))
    task=Task.query.get(task_id)
    if task and task.user_id==user.id:
        db.session.delete(task)
        db.session.commit()
        flash("Task Deleted Successfully","info")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/delete_all",methods=["POST"])
def delete_all_tasks():
    if "user" not in session:
        flash("Please login first", "danger")
        return redirect(url_for("auth.login"))
    
    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        flash("User not found","danger")
        return redirect(url_for("auth.login"))
    Task.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    flash("All Tasks Deleted Successfully", "info")
    return redirect(url_for("task.view_tasks"))

@task_bp.route("/update/<int:task_id>",methods=["POST"])
def update_task(task_id):
    if "user" not in session:
        flash("Please login first", "danger")
        return redirect(url_for("auth.login"))

    from app.models import User
    user = User.query.filter_by(username=session["user"]).first()
    if not user:
        flash("User not found","danger")
        return redirect(url_for("auth.login"))
    task = Task.query.get(task_id)
    if task and task.user_id==user.id:
        new_title = request.form.get("title")
        if new_title:
            task.title = new_title
            db.session.commit()
            flash("Task Updated Successfully", "success")
    return redirect(url_for("task.view_tasks"))