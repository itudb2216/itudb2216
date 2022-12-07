from flask import current_app, render_template


def navigation_page():
    return render_template("navigation.html")
    
def home_page():
    return render_template("home.html")

def club_page():
    myDB = current_app.config["db"]
    clubs = myDB.get_clubs()
    return render_template("club.html", clubs = clubs)

def competition_page():
    myDB = current_app.config["db"]
    competitions = myDB.get_competitions()
    return render_template("competition.html", competitions = competitions)

def game_page():
    myDB = current_app.config["db"]
    games = myDB.get_games()
    return render_template("game.html", games=games)

def player_valuation_page():
    myDB = current_app.config["db"]
    playerValuations = myDB.get_player_valuations()
    return render_template("player_valuation.html", valuations = playerValuations)

def player_page():
    myDB = current_app.config["db"]
    players = myDB.get_players()
    return render_template("player.html", players = players)

def appearance_page():
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    return render_template("appearance.html", appearances = appearances)