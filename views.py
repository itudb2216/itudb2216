from flask import current_app, render_template

def home_page():
    return render_template("home.html")