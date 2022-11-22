class Game:
    def __init__(self, game_id, competition_id, competition_type, season, round, date, home_club_id, away_club_id, home_club_goals, away_club_goals):
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


    def add(self):
        query = "INSERT INTO GAMES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        vars = (self.game_id, self.competition_id, self.competition_type, self.season, self.round, self.date, self.home_club_id, self.away_club_id, self.home_club_goals, self.away_club_goals)
        return query, vars
    
    
    def update(self):
        query = "UPDATE GAMES SET COMPETITION_ID = ?, COMPETITION_TYPE = ?, SEASON = ?, ROUND = ?, DATE = ?, HOME_CLUB_ID = ?, AWAY_CLUB_ID = ?, HOME_CLUB_GOALS = ?, AWAY_CLUB_GOALS = ? WHERE (GAME_ID = ?)"
        vars = (self.competition_id, self.competition_type, self.season, self.round, self.date, self.home_club_id, self.away_club_id, self.home_club_goals, self.away_club_goals, self.game_id)
        return query, vars
    

    def delete(self):
        query = "DELETE FROM MOVIE WHERE (GAME_ID = ?)"
        return query, (self.game_id,)
