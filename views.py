from flask import current_app, render_template, request, session
from tables.club import Club
from tables.competition import Competition
from tables.appearance import Appearance
from tables.player import Player
from tables.game import Game
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
    print("HERE")
    competitions = myDB.get_competitions()
    print("COMPETITION: ", competitions[1])
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

def search_bar():
    return render_template("search.html", element = None, table_name = None, admin = session.get("admin")) # element = None

def search_element():
    if(request.method == "GET"):

        table_name = (request.args)['search_bar']
        primary_key = (request.args)['primary_key']
        myDB = current_app.config["db"]

        if(table_name == 'APPEARANCES'):
            element = myDB.get_appearance(primary_key)
            # primary_key_name = 'appearance_id'

        elif(table_name == 'GAMES'):
            element = myDB.get_game(primary_key)
            # primary_key_name = 'game_id'

        elif(table_name == 'CLUBS'):
            element = myDB.get_club(primary_key)
            # primary_key_name = 'club_id'

        elif(table_name == 'COMPETITIONS'):
            element = myDB.get_competition(primary_key)
            # primary_key_name = 'competition_id'

        elif(table_name == 'PLAYERVALUATIONS'):
            
            element = myDB.get_player_valuation(primary_key)
            # primary_key_name = 'player_valuation_id'

        elif(table_name == 'PLAYERS'):
            element = myDB.get_player(primary_key)
            print("ELEMENT: ", element)
            # primary_key_name = 'player_id'

        # print("ELEMENT: ", element)

        # element = myDB.search_result(table_name, primary_key, primary_key_name)
        return render_template("search.html", element = element, table_name = table_name, admin = session.get("admin"))


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

    print("CURRENT PLAYER VALUATION: ", current_player_valuation)
    return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = True, current_player_valuation = current_player_valuation)

def update_player_valuation(player_valuation_id):
    if(player_valuation_id == "Close"):
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, current_player_valuation = None)

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        
        # print("REQUEST: ", request.form['player_valuation_id'])

        # date_time = (request.form)['date_time']
        # market_value = (request.form)['market_value']
        # date_week = (request.form)['date_week']
        # player_id = (request.form)['player_id']
        # current_club_id = (request.form)['current_club_id']
        # player_club_domestic_competition_id = (request.form)['player_club_domestic_competition_id']
        # new_player_valuation_id = (request.form)['player_valuation_id']

        date_time = (request.args)['date_time']
        market_value = (request.args)['market_value']
        date_week = (request.args)['date_week']
        player_id = (request.args)['player_id']
        current_club_id = (request.args)['current_club_id']
        player_club_domestic_competition_id = (request.args)['player_club_domestic_competition_id']
        new_player_valuation_id = (request.args)['player_valuation_id']

        myDB.update_player_valuation(new_player_valuation_id, player_valuation_id, date_time, market_value, date_week, player_id, current_club_id, player_club_domestic_competition_id)

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
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Club((request.args)['club_id'], (request.args)['name'], (request.args)['pretty_name'], 
                         (request.args)['domestic_competition_id'], (request.args)['total_market_value'], (request.args)['squad_size'], 
                         (request.args)['average_age'], (request.args)['foreigners_number'], (request.args)['foreigners_percentage'], 
                         (request.args)['national_team_players'], (request.args)['stadium_name'], (request.args)['stadium_seats'], 
                         (request.args)['net_transfer_record'], (request.args)['coach_name']), club_id)
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
                         (request.args)['name'], (request.args)['confederation']), competition_id)
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None)

#Appearances

def delete_appearance(appearance_id):
    myDB = current_app.config["db"]
    myDB.delete(myDB.get_appearance(appearance_id))
    return render_template("appearance.html", appearances = myDB.get_appearances(), admin = session.get("admin"), update_form_appearance = False, current_appearance = None)

def update_form_appearance(appearance_id):
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    current_appearance = myDB.get_appearance(appearance_id)
    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = True, current_appearance = current_appearance)

def update_appearance(appearance_id):
    if(appearance_id == "Close"):
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, current_appearance = None)

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Appearance((request.args)['appearance_id'], (request.args)['game_id'], (request.args)['player_id'],
                         (request.args)['player_club_id'], (request.args)['date'], (request.args)['player_pretty_name'], 
                         (request.args)['competition_id'], (request.args)['yellow_cards'], (request.args)['red_cards'], 
                         (request.args)['goals'], (request.args)['assists'], (request.args)['minutes_played']), appearance_id)

        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, current_appearance = None)


# Players 
def delete_player(player_id):
    myDB = current_app.config["db"]
    myDB.delete(myDB.get_player(player_id))
    return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None)
    
def update_form_player(player_id):
    myDB =  current_app.config["db"]
    return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = True, current_player = myDB.get_player(player_id))

def update_player(player_id):
    if (player_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]

        myDB.update(Player((request.args)['player_id'], (request.args)['pretty_name'], (request.args)['club_id'], (request.args)['club_pretty_name'], 
                         (request.args)['current_club_id'], (request.args)['country_of_citizenship'], (request.args)['date_of_birth'], 
                         (request.args)['position'], (request.args)['foot'], (request.args)['height_in_cm'], 
                         (request.args)['market_value_in_gbp'], (request.args)['highest_market_value_in_gbp']), player_id)
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None)

        
#Games

def delete_game(game_id):
    myDB = current_app.config["db"]
    myDB.delete(myDB.get_game(game_id))
    return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None)
    
def update_form_game(game_id):
    myDB =  current_app.config["db"]
    return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = True, current_game = myDB.get_game(game_id))

def update_game(game_id):
    if (game_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Game((request.args)['game_id'], (request.args)['competition_id'], (request.args)['competition_type'], 
                         (request.args)['season'], (request.args)['round'], (request.args)['date'], 
                         (request.args)['home_club_id'], (request.args)['away_club_id'], (request.args)['home_club_goals'], 
                         (request.args)['away_club_goals'], (request.args)['club_home_pretty_name'], (request.args)['club_away_pretty_name'], 
                         (request.args)['stadium']), game_id)
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None)
