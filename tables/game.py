class Game:
    def __init__(self, game_id, competition_id, competition_type, season, round, date, home_club_id,
                away_club_id, home_club_goals, away_club_goals, club_home_pretty_name=None, 
                club_away_pretty_name=None, stadium=None):
        self.game_id = game_id
        self.competition_id = competition_id
        self.competition_type = competition_type
        self.season = season
        self.round = round
        self.date = date
        self.home_club_id = home_club_id
        self.away_club_id = away_club_id
        self.home_club_goals = home_club_goals
        self.away_club_goals = away_club_goals
        self.club_home_pretty_name = club_home_pretty_name
        self.club_away_pretty_name = club_away_pretty_name
        self.stadium = stadium


    def add(self):
        query = "INSERT INTO GAMES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        vars = (self.game_id, self.competition_id, self.competition_type, self.season, self.round, self.date,
            self.home_club_id, self.away_club_id, self.home_club_goals, self.away_club_goals,
            self.club_home_pretty_name, self.club_away_pretty_name, self.stadium)
        return query, vars
    
    
    def update(self):
        query = "UPDATE GAMES SET COMPETITION_ID = ?, COMPETITION_TYPE = ?, SEASON = ?, ROUND = ?, DATE = ?,\
            HOME_CLUB_ID = ?, AWAY_CLUB_ID = ?, HOME_CLUB_GOALS = ?, AWAY_CLUB_GOALS = ?, CLUB_HOME_PRETTY_NAME = ?,\
            CLUB_AWAY_PRETTY_NAME = ?, STADIUM = ? WHERE (GAME_ID = ?)"
        vars = (self.competition_id, self.competition_type, self.season, self.round, self.date, self.home_club_id,
            self.away_club_id, self.home_club_goals, self.away_club_goals, self.club_home_pretty_name,
            self.club_away_pretty_name, self.stadium, self.game_id)
        return query, vars
    

    def delete(self):
        query = "DELETE FROM GAMES WHERE (GAME_ID = ?)"
        return query, (self.game_id,)
