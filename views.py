from flask import current_app, render_template, request, session
from tables.club import Club
from tables.competition import Competition
from tables.appearance import Appearance
def navigation_page():
    # return render_template("navigation.html", admin = admin)
    return render_template("navigation.html", admin = session.get("admin"))
    
def home_page():
    return render_template("home.html", logout = False, login="First", admin = session.get("admin"))

def login_page():
    return render_template("login.html")

def admin_page():
    myDB = current_app.config["db"]
    admins = myDB.get_admins()
    return render_template("admins.html", admins = admins, admin = session.get("admin"))

def admin_check():
    if(request.method == "GET"):
        myDB = current_app.config["db"]
        student_id = (request.args)['student_id']
        password = (request.args)['pass']
        admin = myDB.get_admin(student_id)
        session["admin"] = myDB.get_admin(student_id)

        if(admin == None): # if the student id entered incorrectly, so in database, there is not anyone corresponding to that id
            return render_template("home.html", logout = False, login = "False", admin = admin)

        elif(admin.password == password): # if the password is correct in addition to student id, access granted
            return render_template("home.html", logout = False, login = "True", admin = admin)
        
        else: # if the user id is correctly given, but the password is false, then access denied
            admin = None
            return render_template("home.html", logout = False, login = "False", admin = admin)
        
def log_out(): # this method will be called, when user logs out from "Admin" to normal user
    session["admin"] = None
    admin = None
    return render_template("home.html", logout = True, admin = admin)

def club_page():
    myDB = current_app.config["db"]
    clubs = myDB.get_clubs()
    return render_template("club.html", clubs = clubs, admin = session.get("admin"))

def competition_page():
    myDB = current_app.config["db"]
    competitions = myDB.get_competitions()
    return render_template("competition.html", competitions = competitions, admin = session.get("admin"))

def game_page():
    myDB = current_app.config["db"]
    games = myDB.get_games()
    return render_template("game.html", games=games, admin = session.get("admin"))

def player_valuation_page():
    myDB = current_app.config["db"]
    playerValuations = myDB.get_player_valuations()
    return render_template("player_valuation.html", valuations = playerValuations, admin = session.get("admin"), update_form = False, current_player_valuation = None)

def player_page():
    myDB = current_app.config["db"]
    players = myDB.get_players()
    return render_template("player.html", players = players, admin = session.get("admin"))

def appearance_page():
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"))

#PLAYER VALUATIONS
def delete_player_valuation(player_valuation_id):
    myDB = current_app.config["db"]
    myDB.delete_player_valuation(player_valuation_id)
    player_valuations = myDB.get_player_valuations()
    return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, current_player_valuation = None)

def update_form(player_valuation_id):
    myDB = current_app.config["db"]
    player_valuations = myDB.get_player_valuations()
    current_player_valuation = myDB.get_player_valuation(player_valuation_id)
    return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = True, current_player_valuation = current_player_valuation)

def update_player_valuation(player_valuation_id):
    if(player_valuation_id == "Close"):
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, current_player_valuation = None)

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        new_player_valuation_id = (request.args)['player_valuation_id']
        date_time = (request.args)['date_time']
        market_value = (request.args)['market_value']
        date_week = (request.args)['date_week']
        
        myDB.update_player_valuation(new_player_valuation_id, player_valuation_id, date_time, market_value, date_week)

        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, current_player_valuation = None)

# We need to add try, except, and finally for each function we use cursor !!!

#CLUBS

def delete_club(club_id):
    myDB = current_app.config["db"]
    myDB.delete(myDB.get_club(club_id))
    return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None)

def update_form_club(club_id):
    myDB =  current_app.config["db"]
    return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = True, current_club = myDB.get_club(club_id))

def update_club(club_id):
    if (club_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("club.html", clubs = myDB.get_clubs, admin = session.get("admin"), update_form_club = False, current_club = None)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Club((request.args)['club_id'], (request.args)['name'], (request.args)['pretty_name'], 
                         (request.args)['domestic_competition_id'], (request.args)['total_market_value'], (request.args)['squad_size'], 
                         (request.args)['average_age'], (request.args)['foreigners_number'], (request.args)['foreigners_percentage'], 
                         (request.args)['national_team_players'], (request.args)['stadium_name'], (request.args)['stadium_seats'], 
                         (request.args)['net_transfer_record'], (request.args)['coach_name']))
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None)
    
#COMPETITIONS
    
def delete_competition(competition_id):
    myDB = current_app.config["db"]
    myDB.delete(myDB.get_competition(competition_id))
    return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None)

def update_form_competition(competition_id):
    myDB =  current_app.config["db"]
    return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = True, current_competition = myDB.get_competition(competition_id))

def update_competition(competition_id):
    if (competition_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("competition.html", competitions = myDB.get_competitions, admin = session.get("admin"), update_form_competition = False, current_competition = None)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Competition((request.args)['competition_id'], (request.args)['pretty_name'], (request.args)['type_'],
                         (request.args)['sub_type'], (request.args)['country_id'], (request.args)['country_name'], 
                         (request.args)['country_latitude'], (request.args)['country_longitude'], (request.args)['domestic_league_code'], 
                         (request.args)['name'], (request.args)['confederation']))
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None)
def update_form_appearance(appearance_id):
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    current_appearance = myDB.get_appearance(appearance_id)
    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form = True, current_appearance = current_appearance)

#Appearances

def update_appearance(appearance_id):
    if(appearance_id == "Close"):
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form = False, current_appearance = None)

    if(request.method == "GET"):
        myDB = current_app.config["db"]

        new_appearance_id = (request.args)['appearance_id']
        game_id = (request.args)['game_id']
        player_id = (request.args)['player_id']
        player_club_id = (request.args)['player_club_id']
        date = (request.args)['date']
        
        myDB.update_appearance(appearance_id, new_appearance_id, game_id, player_id, player_club_id, date)

        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form = False, current_appearance = None)
