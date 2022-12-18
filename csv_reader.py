import pandas as pd
import numpy as np
from database import Database
from tables.player import Player
from tables.club import Club
from tables.game import Game
from tables.appearance import Appearance
from tables.player_valuation import PlayerValuation
from tables.competition import Competition
from tables.admin import Admin

myDB = Database('transfermarkt.db')

# Adds from competitions.csv to COMPETITIONS table
competitions = pd.read_csv("csv_files/competitions.csv")
print(competitions.keys())
for A in competitions.values:
    competition = Competition(*A[0:11])
    myDB.add(competition)

# Adds from clubs.csv to CLUBS table
clubs = pd.read_csv("csv_files/clubs.csv")
print(clubs.keys())
for A in clubs.values:
    club = Club(*A[0:14])
    myDB.add(club)

# Adds from players.csv to PLAYERS table
players = pd.read_csv("csv_files/players.csv")
print(players.keys())
players.drop(columns=['url', 'image_url', 'country_of_birth', 'sub_position', 'name',
                    'agent_name', 'contract_expiration_date', 'domestic_competition_id',
                    'club_name', 'last_season'], inplace=True)
print(players.keys())
for A in players.values:
    player = Player(*A[0:12])
    myDB.add(player)

# Adds from games.csv to GAMES table
games = pd.read_csv("csv_files/games.csv")
print(games.keys())
games.drop(columns=["aggregate", "home_club_position", "away_club_position", "home_club_manager_name",
                    "away_club_manager_name", "attendance", "referee", "url"], inplace=True)
print(games.keys())
for A in games.values:
    # print(A)
    game = Game(*A[0:13])
    myDB.add(game)

# Adds from appearances.csv to APPEARANCES table
appearances = pd.read_csv("csv_files/appearances.csv")
print(appearances.keys())
for A in appearances.values:
    appearance = Appearance(*A[0:12])
    myDB.add(appearance)

# Ads from player_valuations.csv to PLAYERVALUATIONS table
player_valuations = pd.read_csv("csv_files/player_valuations.csv")
print(player_valuations.keys())
player_valuations.drop(columns=["date"],inplace=True)
print(player_valuations.keys())
for A in player_valuations.values:
    player_valuation = PlayerValuation(*A[0:6])
    myDB.add(player_valuation)
