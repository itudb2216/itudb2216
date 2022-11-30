from flask import current_app, render_template

def home_page():
    return render_template("home.html")

def appearance_page():
    return render_template("appearance.html")

def club_page():
    return render_template("club.html")

def competition_page():
    return render_template("competition.html")

def game_page():
    return render_template("game.html")

def player_valuation_page():
    return render_template("player_valuation.html")

def player_page():
    return render_template("player.html")