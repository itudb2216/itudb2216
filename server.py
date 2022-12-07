# VERSION 194

from flask import Flask
from database import Database
import views
import os
import sqlite3 as dbapi2

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")
    app.add_url_rule("/", view_func=views.home_page)

    if not os.path.exists('./transfermarkt.db'):
        con = dbapi2.connect("transfermarkt.db")
        con.execute(
            "CREATE TABLE PLAYERS ( player_id INTEGER PRIMARY KEY, pretty_name TEXT NOT NULL,club_id INTEGER NOT NULL,\
            club_pretty_name TEXT NOT NULL,current_club_id INTEGER NOT NULL,country_of_citizenship TEXT NOT NULL,date_of_birth TEXT,\
            position TEXT,foot TEXT,height_in_cm INTEGER,market_value_in_gbp REAL,highest_market_value_in_gbp REAL)\
            FOREIGN KEY(club_id) REFERENCES CLUBS(CLUB_ID),\
            FOREIGN KEY(current_club_id) REFERENCES CLUBS(CLUB_ID)")
        con.execute(
            "CREATE TABLE APPEARANCE ()"
        )
        con.execute(
            "CREATE TABLE GAMES ()"
        )
        con.execute(
            "CREATE TABLE COMPETITION ()"
        )
        con.execute(
            "CREATE TABLE CLUB ()"
        )
        con.execute(
            "CREATE TABLE PLAYERVALUATIONS (player_valuation_id INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT NOT NULL, dateweek TEXT NOT NULL, player_id INTEGER NOT NULL, current_club_id INTEGER NOT NULL, market_value INTEGER NOT NULL, player_club_domestic_competition_id TEXT NOT NULL, FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id))"
        )

        con.close()

    dir = os.getcwd()
    db = Database(os.path.join(dir, "transfermarkt.db"))
    app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT")
    app.run(host = "0.0.0.0", port = port)