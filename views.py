from flask import current_app, render_template, request

admin = None # can be None, or any Tuple (5 different tuples exist, because there are 5 admins in this project)
# Will be used to log in to the page, so only admins can delete and update the tables. Other uses can only see the tables

def navigation_page():
    return render_template("navigation.html", admin = admin)
    
def home_page():
    return render_template("home.html", logout = False, login="First", admin = admin)

def login_page():
    return render_template("login.html")

def admin_page():
    myDB = current_app.config["db"]
    admins = myDB.get_admins()
    return render_template("admins.html", admins = admins, admin = admin)


def admin_check():
    if(request.method == "GET"):
        myDB = current_app.config["db"]
        student_id = (request.args)['student_id']
        password = (request.args)['pass']
        global admin
        admin = myDB.get_admin(student_id)
        if(admin == None): # if the student id entered incorrectly, so in database, there is not anyone corresponding to that id
            return render_template("home.html", logout = False, login = "False", admin = admin)

        elif(admin.password == password): # if the password is correct in addition to student id, access granted
            return render_template("home.html", logout = False, login = "True", admin = admin)
        
        else: # if the user id is correctly given, but the password is false, then access denied
            admin = None
            return render_template("home.html", logout = False, login = "False", admin = admin)
        
def log_out(): # this method will be called, when user logs out from "Admin" to normal user
    global admin
    admin = None
    return render_template("home.html", logout = True, admin = admin)

def club_page():
    myDB = current_app.config["db"]
    clubs = myDB.get_clubs()
    return render_template("club.html", clubs = clubs, admin = admin)

def competition_page():
    myDB = current_app.config["db"]
    competitions = myDB.get_competitions()
    return render_template("competition.html", competitions = competitions, admin = admin)

def game_page():
    myDB = current_app.config["db"]
    games = myDB.get_games()
    return render_template("game.html", games=games, admin = admin)

def player_valuation_page():
    myDB = current_app.config["db"]
    playerValuations = myDB.get_player_valuations()
    return render_template("player_valuation.html", valuations = playerValuations, admin = admin)

def player_page():
    myDB = current_app.config["db"]
    players = myDB.get_players()
    return render_template("player.html", players = players, admin = admin)

def appearance_page():
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    return render_template("appearance.html", appearances = appearances, admin = admin)