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

# competitions = pd.read_csv("csv_files/competitions.csv")
# print(competitions.keys())
# #competitions.drop(columns=[],inplace=True)
# print(competitions.keys())
# for A in competitions.values:
#     competition = Competition(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11])
#     myDB.add(competition)


# clubs = pd.read_csv("csv_files/clubs.csv")
# print(clubs.keys())
# #clubs.drop(columns=[],inplace=True)
# print(clubs.keys())
# for A in clubs.values:
#     club = Club(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11],A[12],A[13],A[14])
#     myDB.add(club)


# players = pd.read_csv("csv_files/players.csv")
# print(players.keys())
# players.drop(columns=['url','image_url','country_of_birth','sub_position','name',
#                     'agent_name', 'contract_expiration_date', 'domestic_competition_id',
#                     'club_name', 'last_season'],inplace=True)
# print(players.keys())
# for A in players.values:
#     player = Player(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11])
#     myDB.add(player)


games = pd.read_csv("csv_files/games.csv")
print(games.keys())
games.drop(columns=["aggregate","home_club_position","away_club_position","home_club_manager_name","away_club_manager_name","attendance","referee","url"],inplace=True)
print(games.keys())
for A in games[9:].values:
    # print(A)
    game = Game(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11],A[12])
    myDB.add(game)


appearances = pd.read_csv("csv_files/appearances.csv")
print(appearances.keys())
#appearance.drop(columns=[],inplace=True)
print(appearances.keys())
for A in appearances.head(100).values:
    appearance = Appearance(A[0],A[1],A[2],A[3],A[4],A[5],A[6],A[7],A[8],A[9],A[10],A[11])
    myDB.add(appearance)


player_valuations = pd.read_csv("csv_files/player_valuations.csv")
print(player_valuations.keys())
player_valuations.drop(columns=["date"],inplace=True)
print(player_valuations.keys())
for A in player_valuations.head(100).values:
    player_valuation = PlayerValuation(A[0],A[1],A[2],A[3],A[4],A[5])
    myDB.add(player_valuation)


