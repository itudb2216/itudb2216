class PlayerValuation:
    def __init__(self, datetime, dateweek, player_id, current_club_id, market_value, player_club_domestic_competition_id):
        # self.player_valuation_id = player_valuation_id #PRIMARY KEY
        self.datetime = datetime
        self.dateweek = dateweek
        self.player_id = player_id # FOREIGN KEY
        self.current_club_id = current_club_id
        self.market_value = market_value
        self.player_club_domestic_competition_id = player_club_domestic_competition_id
        

    def add(self):
        query = "INSERT INTO PLAYERVALUATIONS (DATETIME, DATEWEEK, PLAYER_ID, CURRENT_CLUB_ID, MARKET_VALUE, PLAYER_CLUB_DOMESTIC_COMPETITION_ID) VALUES (?, ?, ?, ?, ?, ?)"
        tup = (self.datetime, self.dateweek, self.player_id, self.current_club_id, self.market_value, self.player_club_domestic_competition_id)
        return query, tup
