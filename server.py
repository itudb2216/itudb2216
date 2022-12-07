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
            "CREATE TABLE PLAYERS ( player_id INTEGER PRIMARY KEY)")
        con.execute(
            "CREATE TABLE APPEARANCES (appearance_id TEXT PRIMARY KEY, game_id INTEGER, player_id INTEGER, player_club_id INTEGER, date DATE, player_pretty_name TEXT, competition_id TEXT, yellow_cards INTEGER, red_cards INTEGER, goals INTEGER, assists INTEGER, minutes_played INTEGER, FOREIGN KEY(game_id) REFERENCES GAMES(game_id), FOREIGN KEY(player_id) REFERENCES PLAYERS(player_id))"
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
            "CREATE TABLE PLAYERVALUATION ()"
        )

        dir = os.getcwd()
        db = Database(os.path.join(dir, "transfermarkt.db"))
        app.config["db"] = db

    return app


if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT")
    app.run(host = "0.0.0.0", port = port)