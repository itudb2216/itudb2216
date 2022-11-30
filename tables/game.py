class Game:
    def __init__(self, game_id, competition_id, competition_type, season, round, date, home_club_id, away_club_id,
                home_club_goals, away_club_goals, aggregate, home_club_position, away_club_position,
                club_home_pretty_name=None, club_away_pretty_name=None, home_club_manager_name=None,
                away_club_manager_name=None, stadium=None, attendance=None, referee=None, url=None):
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
        self.aggregate = aggregate
        self.home_club_position = home_club_position
        self.away_club_position = away_club_position
        self.club_home_pretty_name = club_home_pretty_name
        self.club_away_pretty_name = club_away_pretty_name
        self.home_club_manager_name = home_club_manager_name
        self.away_club_manager_name = away_club_manager_name
        self.stadium = stadium
        self.attendance = attendance
        self.referee = referee
        self.url = url
        


    def add(self):
        query = "INSERT INTO GAMES VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        vars = (self.game_id, self.competition_id, self.competition_type, self.season, self.round, self.date,
            self.home_club_id, self.away_club_id, self.home_club_goals, self.away_club_goals, self.aggregate,
            self.home_club_position, self.away_club_position, self.club_home_pretty_name, self.club_away_pretty_name,
            self.home_club_manager_name, self.away_club_manager_name, self.stadium, self.attendance, self.referee, self.url)
        return query, vars
    
    
    def update(self):
        query = "UPDATE GAMES SET COMPETITION_ID = ?, COMPETITION_TYPE = ?, SEASON = ?, ROUND = ?, DATE = ?,\
            HOME_CLUB_ID = ?, AWAY_CLUB_ID = ?, HOME_CLUB_GOALS = ?, AWAY_CLUB_GOALS = ?, AGGREGATE = ?,\
                HOME_CLUB_POSITION = ?, AWAY_CLUB_POSITION = ?, CLUB_HOME_PRETTY_NAME = ?, CLUB_AWAY_PRETTY_NAME = ?\
                    HOME_CLUB_MANAGER_NAME = ?, AWAY_CLUB_MANAGER_NAME = ?, STADIUM = ?, ATTENDANCE = ?, REFEREE = ?,\
                        URL = ? WHERE (GAME_ID = ?)"
        vars = (self.competition_id, self.competition_type, self.season, self.round, self.date, self.home_club_id,
            self.away_club_id, self.home_club_goals, self.away_club_goals, self.aggregate, self.home_club_position,
            self.away_club_position, self.club_home_pretty_name, self.club_away_pretty_name, self.home_club_manager_name,
            self.away_club_manager_name, self.stadium, self.attendance, self.referee, self.url, self.game_id)
        return query, vars
    

    def delete(self):
        query = "DELETE FROM MOVIE WHERE (GAME_ID = ?)"
        return query, (self.game_id,)
