from flask import current_app, render_template, request, session
from tables.club import Club
from tables.competition import Competition
from tables.appearance import Appearance
from tables.player import Player
from tables.game import Game
from tables.player_valuation import PlayerValuation
import math

def navigation_page():
    return render_template("navigation.html", admin = session.get("admin"))
    
def home_page():
    session['page_number_player_valuation'] = 0
    session['page_number_player'] = 0
    session['page_number_appearance'] = 0
    session['page_number_club'] = 0
    session['page_number_competition'] = 0
    session['page_number_game'] = 0

    session['sort_table'] = None
    session['sort_key'] = None
    session['sort_order'] = None

    return render_template("home.html", logout = False, login="First", admin = session.get("admin"))

def login_page():
    return render_template("login.html")

def admin_page():
    myDB = current_app.config["db"]
    admins = myDB.get_admins()
    return render_template("admins.html", admins = admins, admin = session.get("admin"))

# Checks access for admin
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

# This method will be called, when user logs out from "Admin" to normal user
def log_out():
    session["admin"] = None
    admin = None
    return render_template("home.html", logout = True, admin = admin)

def club_page():
    myDB = current_app.config["db"]
    clubs = myDB.get_clubs()
    return render_template("club.html", clubs = clubs, admin = session.get("admin"), from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)

def competition_page():
    myDB = current_app.config["db"]
    competitions = myDB.get_competitions()
    return render_template("competition.html", competitions = competitions, admin = session.get("admin"),  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)

def game_page():
    myDB = current_app.config["db"]
    games = myDB.get_games()
    return render_template("game.html", games=games, admin = session.get("admin"), from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)

def player_valuation_page():
    myDB = current_app.config["db"]
    playerValuations = myDB.get_player_valuations()
    return render_template("player_valuation.html", valuations = playerValuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

def player_page():
    myDB = current_app.config["db"]
    players = myDB.get_players()
    return render_template("player.html", players = players, admin = session.get("admin"), from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)

def appearance_page():
    myDB = current_app.config["db"]
    appearances = myDB.get_appearances()
    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)

def search_bar():
    return render_template("search.html", element = None, table_name = None, admin = session.get("admin")) # element = None

# Calls the associated getter for the element whose id (primary key) is searched in a specific table
def search_element():
    if(request.method == "GET"):
        try:
            table_name = (request.args)['search_bar']
            primary_key = (request.args)['primary_key']
            myDB = current_app.config["db"]
            
            if(table_name == 'APPEARANCES'):
                element = myDB.get_appearance(primary_key)

            elif(table_name == 'GAMES'):
                element = myDB.get_game(primary_key)

            elif(table_name == 'CLUBS'):
                element = myDB.get_club(primary_key)

            elif(table_name == 'COMPETITIONS'):
                element = myDB.get_competition(primary_key)

            elif(table_name == 'PLAYERVALUATIONS'):
                
                element = myDB.get_player_valuation(primary_key)

            elif(table_name == 'PLAYERS'):
                element = myDB.get_player(primary_key)

            return render_template("search.html", element = element, table_name = table_name, admin = session.get("admin"))
        except KeyError:
            return render_template("error.html", errorMessage = "seach_bar_incomplete_args")
        except:
            return render_template("error.html", errorMessage = "search_bar_error")

# Necessary functions for delete and update operations in PLAYERVALUATIONS
# delete_*: Calls the necessary delete function from database.py using the id passed parameter and re-generates output
# update_form_*: Method for the page that user is directed to to get into the program the updated versions of the fields
# update_*: Creates new Club, Game, ... object and calls the necessary update function from database.py using the old id passed as parameter and re-generates output

# For PLAYERVALUATIONS

def delete_player_valuation(player_valuation_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete_player_valuation(player_valuation_id)
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))
    except:
        return render_template("error.html", errorMessage = "delete_tuple")
        
def update_form(player_valuation_id):
    try:
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        current_player_valuation = myDB.get_player_valuation(player_valuation_id)
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = True, add_form = False, current_player_valuation = current_player_valuation, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_player_valuation(player_valuation_id):
    if(player_valuation_id == "Close"):
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        date_time = (request.args)['date_time']
        market_value = (request.args)['market_value']
        date_week = (request.args)['date_week']
        player_id = (request.args)['player_id']
        current_club_id = (request.args)['current_club_id']
        player_club_domestic_competition_id = (request.args)['player_club_domestic_competition_id']
        new_player_valuation_id = (request.args)['player_valuation_id']

        myDB.update_player_valuation(new_player_valuation_id, player_valuation_id, date_time, market_value, date_week, player_id, current_club_id, player_club_domestic_competition_id)

        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

# For CLUBS

def delete_club(club_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete(myDB.get_club(club_id))
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "delete_tuple")

def update_form_club(club_id):
    try:
        myDB =  current_app.config["db"]
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = True, current_club = myDB.get_club(club_id), from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_club(club_id):
    if (club_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Club((request.args)['club_id'], (request.args)['name'], (request.args)['pretty_name'], 
                         (request.args)['domestic_competition_id'], (request.args)['total_market_value'], (request.args)['squad_size'], 
                         (request.args)['average_age'], (request.args)['foreigners_number'], (request.args)['foreigners_percentage'], 
                         (request.args)['national_team_players'], (request.args)['stadium_name'], (request.args)['stadium_seats'], 
                         (request.args)['net_transfer_record'], (request.args)['coach_name']), club_id)
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    
# For COMPETITIONS
    
def delete_competition(competition_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete(myDB.get_competition(competition_id))
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "delete_tuple")

def update_form_competition(competition_id):
    try:
        myDB =  current_app.config["db"]
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = True, current_competition = myDB.get_competition(competition_id),  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_competition(competition_id):
    if (competition_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("competition.html", competitions = myDB.get_competitions, admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Competition((request.args)['competition_id'], (request.args)['pretty_name'], (request.args)['type_'],
                         (request.args)['sub_type'], (request.args)['country_id'], (request.args)['country_name'], 
                         (request.args)['country_latitude'], (request.args)['country_longitude'], (request.args)['domestic_league_code'], 
                         (request.args)['name'], (request.args)['confederation']), competition_id)
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)

# For APPEARANCES

def delete_appearance(appearance_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete(myDB.get_appearance(appearance_id))
        return render_template("appearance.html", appearances = myDB.get_appearances(), admin = session.get("admin"), update_form_appearance = False, current_appearance = None, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "delete_tuple")

def update_form_appearance(appearance_id):
    try:
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        current_appearance = myDB.get_appearance(appearance_id)
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = True, current_appearance = current_appearance, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_appearance(appearance_id):
    if(appearance_id == "Close"):
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, current_appearance = None, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Appearance((request.args)['appearance_id'], (request.args)['game_id'], (request.args)['player_id'],
                         (request.args)['player_club_id'], (request.args)['date'], (request.args)['player_pretty_name'], 
                         (request.args)['competition_id'], (request.args)['yellow_cards'], (request.args)['red_cards'], 
                         (request.args)['goals'], (request.args)['assists'], (request.args)['minutes_played']), appearance_id)

        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, current_appearance = None, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)

# For PLAYERS 
def delete_player(player_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete(myDB.get_player(player_id))
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None, from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "delete_tuple")

def update_form_player(player_id):
    try:
        myDB =  current_app.config["db"]
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = True, current_player = myDB.get_player(player_id), from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_player(player_id):
    if (player_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None, from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]

        myDB.update(Player((request.args)['player_id'], (request.args)['pretty_name'], (request.args)['club_id'], (request.args)['club_pretty_name'], 
                         (request.args)['current_club_id'], (request.args)['country_of_citizenship'], (request.args)['date_of_birth'], 
                         (request.args)['position'], (request.args)['foot'], (request.args)['height_in_cm'], 
                         (request.args)['market_value_in_gbp'], (request.args)['highest_market_value_in_gbp']), player_id)
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None, from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)

# For GAMES

def delete_game(game_id):
    try:
        myDB = current_app.config["db"]
        myDB.delete(myDB.get_game(game_id))
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None, from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "delete_tuple")
    
def update_form_game(game_id):
    try:
        myDB =  current_app.config["db"]
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = True, current_game = myDB.get_game(game_id), from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def update_game(game_id):
    if (game_id == "Close"):
        myDB = current_app.config["db"]
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None, from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.update(Game((request.args)['game_id'], (request.args)['competition_id'], (request.args)['competition_type'], 
                         (request.args)['season'], (request.args)['round'], (request.args)['date'], 
                         (request.args)['home_club_id'], (request.args)['away_club_id'], (request.args)['home_club_goals'], 
                         (request.args)['away_club_goals'], (request.args)['club_home_pretty_name'], (request.args)['club_away_pretty_name'], 
                         (request.args)['stadium']), game_id)
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None, from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"),add_form = False)

# Method to call the relevant sorted_get_* method and re-generate output
def sorted_tab():
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        sort_table = (request.args)['sort_table']
        sort_key = (request.args)['sort_key']
        sort_order = (request.args)['asc_desc']

        session['sort_table'] = sort_table
        session['sort_key'] = sort_key
        session['sort_order'] = sort_order

        if(sort_table == "PLAYERVALUATIONS"):
            playerValuations = myDB.sorted_get_player_valuations(sort_table, sort_key, sort_order)
            return render_template("player_valuation.html", valuations = playerValuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

        elif(sort_table == "CLUBS"):
            clubs = myDB.sorted_get_clubs(sort_table, sort_key, sort_order)
            return render_template("club.html", clubs = clubs, admin = session.get("admin"), from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)

        elif(sort_table == "COMPETITIONS"):
            competitions = myDB.sorted_get_competitions(sort_table, sort_key, sort_order)
            return render_template("competition.html", competitions = competitions, admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)

        elif(sort_table == "GAMES"):
            games = myDB.sorted_get_games(sort_table, sort_key, sort_order)
            return render_template("game.html", games=games, admin = session.get("admin"), from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)

        elif(sort_table == "PLAYERS"):
            players = myDB.sorted_get_players(sort_table, sort_key, sort_order)
            return render_template("player.html", players = players, admin = session.get("admin"), from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)

        elif(sort_table == "APPEARANCES"):
            appearances = myDB.sorted_get_appearances(sort_table, sort_key, sort_order)
            return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)

# Methods to increase/decrease the number of tuples shown

def increase_number_player_valuation(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "PLAYERVALUATIONS"):
        playerValuations = myDB.sorted_get_player_valuations(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        playerValuations = myDB.get_player_valuations()

    if(number == ( math.floor(len(playerValuations) / 1000))   - 1):
        from_number = number*1000
        to_number = len(playerValuations) 
        number = number

    elif(number == ( math.floor(len(playerValuations) / 100))):
        from_number = number*100
        to_number = len(playerValuations) 
        number = number

    else:
        from_number = (number * 1000) + 1000
        to_number = (number * 1000) + 2000
        number += 1

    session['page_number_player_valuation'] = number
    
    return render_template("player_valuation.html", valuations = playerValuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = from_number, to_number = to_number, page_number = number)

def decrease_number_player_valuation(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "PLAYERVALUATIONS"):
        playerValuations = myDB.sorted_get_player_valuations(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        playerValuations = myDB.get_player_valuations()
    if(number == 0):
        from_number = 0
        if(len(playerValuations) <= 1000):
            to_number = len(playerValuations)
        else:
            to_number = 1000
        number = 0

    else:
        from_number = ((number-1)*1000)
        to_number = number*1000
        number -= 1

    session['page_number_player_valuation'] = number
    
    return render_template("player_valuation.html", valuations = playerValuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = from_number, to_number = to_number, page_number = number)

def increase_number_game(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "GAMES"):
        games = myDB.sorted_get_games(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        games = myDB.get_games()

    if(number == ( math.floor(len(games) / 1000)) - 1):
        from_number = number*1000
        to_number = len(games) 
        number = number

    elif(number == ( math.floor(len(games) / 100))):
        from_number = number*100
        to_number = len(games) 
        number = number

    else:
        from_number = (number * 1000) + 1000
        to_number = (number * 1000) + 2000
        number += 1

    session['page_number_game'] = number

    return render_template("game.html", games=games, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def decrease_number_game(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "GAMES"):
        games = myDB.sorted_get_games(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        games = myDB.get_games()

    if(number == 0):
        from_number = 0
        if(len(games) <= 1000):
            to_number = len(games)
        else:
            to_number = 1000
        number = 0

    else:
        from_number = ((number-1)*1000)
        to_number = number*1000
        number -= 1

    session['page_number_game'] = number

    return render_template("game.html", games=games, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def increase_number_club(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "CLUBS"):
        clubs = myDB.sorted_get_clubs(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        clubs = myDB.get_clubs()

    if(number == ( math.floor(len(clubs) / 100)) - 1):
        from_number = (number + 1)*100
        to_number = len(clubs) 
        number = number + 1

    elif(number == ( math.floor(len(clubs) / 100))):
        from_number = number*100
        to_number = len(clubs) 
        number = number

    else:
        from_number = (number * 100) + 100
        to_number = (number * 100) + 200
        number += 1

    session["page_number_club"] = number

    return render_template("club.html", clubs = clubs, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def decrease_number_club(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "CLUBS"):
        clubs = myDB.sorted_get_clubs(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        clubs = myDB.get_clubs()

    if(number == 0):
        from_number = 0
        if(len(clubs) <= 100):
            to_number = len(clubs)
        else:
            to_number = 100
        number = 0

    else:
        from_number = ((number-1)*100)
        to_number = number*100
        number -= 1

    session["page_number_club"] = number

    return render_template("club.html", clubs = clubs, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def increase_number_competition(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "COMPETITIONS"):
        competitions = myDB.sorted_get_competitions(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        competitions = myDB.get_competitions()

    if(number == ( math.floor(len(competitions) / 100)) - 1):
        from_number = number*100
        to_number = len(competitions) 
        number = number

    elif(number == ( math.floor(len(competitions) / 100))):
        from_number = number*100
        to_number = len(competitions) 
        number = number

    else:
        from_number = (number * 100) + 100
        to_number = (number * 100) + 200
        number += 1

    session['page_number_competition'] = number

    return render_template("competition.html", competitions = competitions, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def decrease_number_competition(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "COMPETITIONS"):
        competitions = myDB.sorted_get_competitions(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        competitions = myDB.get_competitions()

    if(number == 0):
        from_number = 0
        if(len(competitions) <= 100):
            to_number = len(competitions)
        else:
            to_number = 100
        number = 0

    else:
        from_number = ((number-1)*100)
        to_number = number*100
        number -= 1

    session['page_number_competition'] = number

    return render_template("competition.html", competitions = competitions, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def increase_number_appearance(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "APPEARANCES"):
        appearances = myDB.sorted_get_appearances(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        appearances = myDB.get_appearances()

    if(number == ( math.floor(len(appearances) / 100)) - 1):
        from_number = number*100
        to_number = len(appearances) 
        number = number

    elif(number == ( math.floor(len(appearances) / 100))):
        from_number = number*100
        to_number = len(appearances) 
        number = number

    else:
        from_number = (number * 100) + 100
        to_number = (number * 100) + 200
        number += 1

    session["page_number_appearance"] = number

    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)
        
def decrease_number_appearance(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "APPEARANCES"):
        appearances = myDB.sorted_get_appearances(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        appearances = myDB.get_appearances()

    if(number == 0):
        from_number = 0
        if(len(appearances) <= 100):
            to_number = len(appearances)
        else:
            to_number = 100
        number = 0

    else:
        from_number = ((number-1)*100)
        to_number = number*100
        number -= 1

    session["page_number_appearance"] = number

    return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)
    
def increase_number_player(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "PLAYERS"):
        players = myDB.sorted_get_players(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        players = myDB.get_players()

    if(number == ( math.floor(len(players) / 1000)) - 1):
        from_number = number*1000
        to_number = len(players) 
        number = number

    elif(number == ( math.floor(len(players) / 100))):
        from_number = number*100
        to_number = len(players) 
        number = number

    else:
        from_number = (number * 1000) + 1000
        to_number = (number * 1000) + 2000
        number += 1

    session['page_number_player'] = number

    return render_template("player.html", players = players, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)

def decrease_number_player(page_number):
    number = int(page_number)
    myDB = current_app.config["db"]

    if(session.get("sort_table") == "PLAYERS"):
        players = myDB.sorted_get_players(session.get("sort_table"), session.get("sort_key"), session.get("sort_order"))
    else:
        players = myDB.get_players()

    if(number == 0):
        from_number = 0
        if(len(players) <= 1000):
            to_number = len(players)
        else:
            to_number = 1000
        number = 0

    else:
        from_number = ((number-1)*1000)
        to_number = number*1000
        number -= 1

    session['page_number_player'] = number

    return render_template("player.html", players = players, admin = session.get("admin"), from_number = from_number, to_number = to_number, page_number = number, add_form = False)


def add_form_player_valuation():
    try:
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = True, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_player_valuation(todo):
    if(todo == "Close"):
        myDB = current_app.config["db"]
        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        date_time = (request.args)['date_time']
        market_value = (request.args)['market_value']
        date_week = (request.args)['date_week']
        player_id = (request.args)['player_id']
        current_club_id = (request.args)['current_club_id']
        player_club_domestic_competition_id = (request.args)['player_club_domestic_competition_id']

        myDB.add(PlayerValuation(date_time, date_week, player_id, current_club_id, market_value, player_club_domestic_competition_id))

        player_valuations = myDB.get_player_valuations()
        return render_template("player_valuation.html", valuations = player_valuations, admin = session.get("admin"), update_form = False, add_form = False, current_player_valuation = None, from_number = session.get("page_number_player_valuation") * 1000, to_number = session.get("page_number_player_valuation") * 1000 + 1000, page_number = session.get("page_number_player_valuation"))

def add_form_appearance():
    try:
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, add_form = True,current_appearance = None, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"))
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_appearance(todo):
    if(todo == "Close"):
        myDB = current_app.config["db"]
        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"), add_form = False)

    if(request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.add(Appearance((request.args)['appearance_id'], (request.args)['game_id'], (request.args)['player_id'],
                         (request.args)['player_club_id'], (request.args)['date'], (request.args)['player_pretty_name'], 
                         (request.args)['competition_id'], (request.args)['yellow_cards'], (request.args)['red_cards'], 
                         (request.args)['goals'], (request.args)['assists'], (request.args)['minutes_played']))

        appearances = myDB.get_appearances()
        return render_template("appearance.html", appearances = appearances, admin = session.get("admin"), update_form_appearance = False, add_form = False,current_appearance = None, from_number = session.get("page_number_appearance"), to_number = session.get("page_number_appearance") + 100, page_number = session.get("page_number_appearance"))

def add_form_club():
    try:
        myDB =  current_app.config["db"]
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, add_form = True, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"))
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_club(todo):
    if (todo == "Close"):
        myDB = current_app.config["db"]
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.add(Club((request.args)['club_id'], (request.args)['name'], (request.args)['pretty_name'], 
                         (request.args)['domestic_competition_id'], (request.args)['total_market_value'], (request.args)['squad_size'], 
                         (request.args)['average_age'], (request.args)['foreigners_number'], (request.args)['foreigners_percentage'], 
                         (request.args)['national_team_players'], (request.args)['stadium_name'], (request.args)['stadium_seats'], 
                         (request.args)['net_transfer_record'], (request.args)['coach_name']))
        return render_template("club.html", clubs = myDB.get_clubs(), admin = session.get("admin"), update_form_club = False, current_club = None, from_number = session.get("page_number_club") * 100, to_number = session.get("page_number_club") * 100 + 100, page_number = session.get("page_number_club"), add_form = False)
    
def add_form_competition():
    try:
        myDB =  current_app.config["db"]
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"),  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = True)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_competition(todo):
    if (todo == "Close"):
        myDB = current_app.config["db"]
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.add(Competition((request.args)['competition_id'], (request.args)['pretty_name'], (request.args)['type_'],
                         (request.args)['sub_type'], (request.args)['country_id'], (request.args)['country_name'], 
                         (request.args)['country_latitude'], (request.args)['country_longitude'], (request.args)['domestic_league_code'], 
                         (request.args)['name'], (request.args)['confederation']))
        return render_template("competition.html", competitions = myDB.get_competitions(), admin = session.get("admin"), update_form_competition = False, current_competition = None,  from_number = session.get("page_number_competition") * 1000, to_number = session.get("page_number_competition") * 1000 + 1000, page_number = session.get("page_number_competition"), add_form = False)

def add_form_game():
    try:
        myDB =  current_app.config["db"]
        return render_template("game.html", games=myDB.get_games(), admin = session.get("admin"), from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = True)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_game(todo):
    if (todo == "Close"):
        myDB = current_app.config["db"]
        return render_template("game.html", games=myDB.get_games(), admin = session.get("admin"), from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.add(Game((request.args)['game_id'], (request.args)['competition_id'], (request.args)['competition_type'], 
                         (request.args)['season'], (request.args)['round'], (request.args)['date'], 
                         (request.args)['home_club_id'], (request.args)['away_club_id'], (request.args)['home_club_goals'], 
                         (request.args)['away_club_goals'], (request.args)['club_home_pretty_name'], (request.args)['club_away_pretty_name'], 
                         (request.args)['stadium']))
        return render_template("game.html", games = myDB.get_games(), admin = session.get("admin"), update_form_game = False, current_game = None, from_number = session.get("page_number_game") * 1000, to_number = session.get("page_number_game") * 1000 + 1000, page_number = session.get("page_number_game"), add_form = False)

def add_form_player():
    try:
        myDB =  current_app.config["db"]
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = True)
    except:
        return render_template("error.html", errorMessage = "update_tuple")

def add_player(todo):
    if (todo == "Close"):
        myDB = current_app.config["db"]
        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None, from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)
    
    if (request.method == "GET"):
        myDB = current_app.config["db"]
        myDB.add(Player((request.args)['player_id'], (request.args)['pretty_name'], (request.args)['club_id'], (request.args)['club_pretty_name'], 
                         (request.args)['current_club_id'], (request.args)['country_of_citizenship'], (request.args)['date_of_birth'], 
                         (request.args)['position'], (request.args)['foot'], (request.args)['height_in_cm'], 
                         (request.args)['market_value_in_gbp'], (request.args)['highest_market_value_in_gbp']))

        return render_template("player.html", players = myDB.get_players(), admin = session.get("admin"), update_form_player = False, current_player = None, from_number = session.get("page_number_player") * 1000, to_number = session.get("page_number_player") * 1000 + 1000, page_number = session.get("page_number_player"), add_form = False)
