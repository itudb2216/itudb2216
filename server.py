# VERSION 194

from flask import Flask
from database import Database
import views
import os
import sqlite3 as dbapi2
from tables.player_valuation import PlayerValuation

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)
    app.add_url_rule("/valuation", view_func=views.player_valuation_page)
    app.add_url_rule("/bilal", view_func=views.player_page)
    app.add_url_rule("/appearance", view_func=views.appearance_page)

    if not os.path.exists('./transfermarkt.db'):
        con = dbapi2.connect("transfermarkt.db")
        con.execute(
            "CREATE TABLE PLAYERS ( player_id INTEGER PRIMARY KEY, pretty_name TEXT NOT NULL,club_id INTEGER NOT NULL,\
            club_pretty_name TEXT NOT NULL,current_club_id INTEGER NOT NULL,country_of_citizenship TEXT NOT NULL,date_of_birth TEXT,\
            position TEXT,foot TEXT,height_in_cm INTEGER,market_value_in_gbp REAL,highest_market_value_in_gbp REAL,\
            FOREIGN KEY(club_id) REFERENCES CLUBS(CLUB_ID),\
            FOREIGN KEY(current_club_id) REFERENCES CLUBS(CLUB_ID))")
        con.execute(
            "CREATE TABLE APPEARANCES (appearance_id TEXT PRIMARY KEY, game_id INTEGER, player_id INTEGER, player_club_id INTEGER, date DATE, player_pretty_name TEXT, competition_id TEXT, yellow_cards INTEGER, red_cards INTEGER, goals INTEGER, assists INTEGER, minutes_played INTEGER, FOREIGN KEY(game_id) REFERENCES GAMES(game_id), FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id))"
        )
        con.execute(
            "CREATE TABLE GAMES (\
                GAME_ID INTEGER PRIMARY KEY,\
                COMPETITION_ID TEXT NOT NULL,\
                COMPETITION_TYPE TEXT NOT NULL,\
                SEASON INTEGER NOT NULL,\
                ROUND TEXT NOT NULL,\
                DATE TEXT NOT NULL,\
                HOME_CLUB_ID INTEGER NOT NULL,\
                AWAY_CLUB_ID INTEGER NOT NULL,\
                HOME_CLUB_GOALS INTEGER NOT NULL,\
                AWAY_CLUB_GOALS INTEGER NOT NULL,\
                AGGREGATE TEXT NOT NULL,\
                HOME_CLUB_POSITION INTEGER NOT NULL,\
                AWAY_CLUB_POSITION INTEGER NOT NULL,\
                CLUB_HOME_PRETTY_NAME TEXT,\
                CLUB_AWAY_PRETTY_NAME TEXT,\
                HOME_CLUB_MANAGER_NAME TEXT,\
                AWAY_CLUB_MANAGER_NAME TEXT,\
                STADIUM TEXT,\
                ATTENDANCE INTEGER NOT NULL,\
                REFEREE TEXT,\
                URL TEXT NOT NULL,\
                FOREIGN KEY(COMPETITION_ID) REFERENCES COMPETITIONS(COMPETITION_ID),\
                FOREIGN KEY(HOME_CLUB_ID) REFERENCES CLUBS(CLUB_ID),\
                FOREIGN KEY(AWAY_CLUB_ID) REFERENCES CLUBS(CLUB_ID)\
            )"
        )
        con.execute(
            "CREATE TABLE COMPETITION (COMPETITION_ID TEXT PRIMARY KEY, PRETTY_NAME TEXT NOT NULL, TYPE_ TEXT NOT NULL, SUB_TYPE TEXT NOT NULL, COUNTRY_ID INTEGER DEFAULT -1, COUNTRY_NAME TEXT, COUNTRY_LATITUDE REAL, COUTNRY LONGITUDE REAL, DOMESTIC_LEAGUE_CODE TEXT, NAME TEXT, CONFEDERATION TEXT, URL TEXT)"
        )
        con.execute(
            "CREATE TABLE CLUBS (CLUB_ID INTEGER PRIMARY KEY, NAME TEXT NOT NULL, PRETTY_NAME TEXT NOT NULL, DOMESTIC_COMPETITION_ID TEXT NOT NULL, TOTAL_MARKET_VALUE REAL, SQUAD_SIZE INTEGER, AVERAGE_AGE REAL, FOREIGNERS_NUMBER INTEGER, FOREIGNERS_PERCENTAGE REAL, NATIONAL_TEAM_PLAYERS INTEGER, STADIUM_NAME TEXT, STADIUM_SEATS INTEGER, NET_TRANSFER_RECORD TEXT, COACH_NAME TEXT, URL TEXT, FOREIGN KEY (DOMESTIC_COMPETITION_ID) REFERENCES COMPETITION (COMPETITION_ID))"
        )
        con.execute(
            "CREATE TABLE PLAYERVALUATIONS (player_valuation_id INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT NOT NULL, dateweek TEXT NOT NULL, player_id INTEGER NOT NULL, current_club_id INTEGER NOT NULL, market_value INTEGER NOT NULL, player_club_domestic_competition_id TEXT NOT NULL, FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id))"
        )

        con.close()


    dir = os.getcwd()
    db = Database(os.path.join(dir, "transfermarkt.db"))

    db.add(PlayerValuation("24.02.04", "1.2.3", 2, 3, 100, "NA2"))

    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT")
    app.run(host = "0.0.0.0", port = port)