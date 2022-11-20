import psycopg2 as dbapi2

from tables.club import Club
from tables.game import Game
from tables.appearance import Appearance
from tables.player import Player

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile  

    def add(self, object):
        string, tupel = object.add()
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string
            cursor.execute(query, tupel)
            connection.commit()

    def update(self, object):
        string, tupel = object.update()
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string
            cursor.execute(query, tupel)
            connection.commit()

    def delete(self, object):
        string, object_id = object.delete()
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string 
            cursor.execute(query, (object_id,))
            connection.commit()

    def get_club(self, club_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM CLUB WHERE (CLUB_ID = ?)"
            cursor.execute(query, (club_id,))
            club_values = list(cursor.fetchone())
        club_ = Club(*club_values)
        return club_
    
    def get_game(self, game_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM GAMES WHERE (GAME_ID = ?)"
            cursor.execute(query, (game_id,))
            attributes = list(cursor.fetchone())
        game_ = Game(*attributes)
        return game_

    def get_appearance(self, appearance_key):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM APPEARANCE WHERE (appearance_id = ?)"
            cursor.execute(query, (appearance_key,))
            apperance_values = list(cursor.fetchone())
        appearance_ = Appearance(*apperance_values)
        return appearance_
    
    def get_player(self, player_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS WHERE (players_id = ?)"
            cursor.execute(query, (player_id,))
            attributes = list(cursor.fetchone())
        player_ = Player(*attributes)
        return player_
