import sqlite3 as dbapi2

from tables.club import Club
from tables.game import Game
from tables.appearance import Appearance
from tables.player import Player
from tables.player_valuation import PlayerValuation
from tables.competition import Competition

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
            query = "SELECT * FROM CLUBS WHERE (CLUB_ID = ?)"
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

    def get_appearance(self, appearance_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM APPEARANCES WHERE (appearance_id = ?)"
            cursor.execute(query, (appearance_id,))
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

    def get_player_valuation(self, player_valuation_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERVALUATIONS WHERE (PLAYER_VALUATION_ID = ?)"
            cursor.execute(query, (player_valuation_id,))
            player_valuation_values = list(cursor.fetchone())
        player_valuation_ = PlayerValuation(*player_valuation_values)
        return player_valuation_ 

    def get_competition(self, competition_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM COMPETITIONS WHERE (COMPETITOIN_ID = ?)"
            cursor.execute(query, (competition_id,))
            competition_values = list(cursor.fetchone())
        competition_ = Competition(*competition_values)
        return competition_

    def get_clubs(self):
        clubs = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM CLUBS ORDER BY CLUB_ID"
            cursor.execute(query)
            for club_id, name, pretty_name, domestic_competition_id, total_market_value , squad_size , average_age , foreigners_number , foreigners_percentage , national_team_players , stadium_name , stadium_seats , net_transfer_record , coach_name , url in cursor:
                clubs.append(Club(club_id, name, pretty_name, domestic_competition_id, total_market_value , squad_size , average_age , foreigners_number , foreigners_percentage , national_team_players , stadium_name , stadium_seats , net_transfer_record , coach_name , url))
        return clubs

    def get_games(self):
        games = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM GAMES ORDER BY GAME_ID"
            cursor.execute(query)
            for game_id, competition_id, competition_type, season, round, date, home_club_id, away_club_id, home_club_goals, away_club_goals, aggregate, home_club_position, away_club_position, club_home_pretty_name, club_away_pretty_name, home_club_manager_name, away_club_manager_name, stadium, attendance, referee, url in cursor:
                games.append(Game(game_id, competition_id, competition_type, season, round, date, home_club_id, away_club_id, home_club_goals, away_club_goals, aggregate, home_club_position, away_club_position, club_home_pretty_name, club_away_pretty_name, home_club_manager_name, away_club_manager_name, stadium, attendance, referee, url))
        return games
    
    def get_appearances(self):
        appearances = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM APPEARANCES ORDER BY APPEARANCE_ID"
            cursor.execute(query)
            for appearance_id, game_id, player_id, player_club_id, date, player_pretty_name, competition_id, yellow_cards, red_cards, goals, assists, minutes_played in cursor:
                appearances.append(Appearance(appearance_id, game_id, player_id, player_club_id, date, player_pretty_name, competition_id, yellow_cards, red_cards, goals, assists, minutes_played))
        return appearances
    
    def get_players(self):
        players = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERS ORDER BY PLAYER_ID"
            cursor.execute(query)
            for player_id, pretty_name, club_id, club_pretty_name, current_club_id, country_of_citizenship, date_of_birth, position, foot, height_in_cm, market_value_in_gbp, highest_market_value_in_gbp in cursor:
                players.append(Player(player_id, pretty_name, club_id, club_pretty_name, current_club_id, country_of_citizenship, date_of_birth, position, foot, height_in_cm, market_value_in_gbp, highest_market_value_in_gbp))
        return players
    
    def get_player_valuations(self):
        player_valuations = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM PLAYERVALUATIONS ORDER BY PLAYER_VALUATION_ID"
            cursor.execute(query)
            for player_valuation_id, datetime, dateweek, player_id, current_club_id, market_value, player_club_domestic_competition_id in cursor:
                player_valuations.append(PlayerValuation(player_valuation_id, datetime, dateweek, player_id, current_club_id, market_value, player_club_domestic_competition_id))
        return player_valuations

    def get_competitions(self):
        competitions = []
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM COMPETITIONS ORDER BY COMPETITION_ID"
            cursor.execute(query)
            for competition_id, pretty_name, type_, sub_type, country_id, country_name, country_latitude, country_longitude, domestic_league_code, name, confederation, url in cursor:
                competitions.append(Player(competition_id, pretty_name, type_, sub_type, country_id, country_name, country_latitude, country_longitude, domestic_league_code, name, confederation, url))
        return competitions