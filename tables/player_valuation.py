class PlayerValuation:
    def __init__(self, player_valuation_id, datetime, dateweek, player_id, current_club_id, market_value, player_club_domestic_competition_id):
        self.player_valuation_id = player_valuation_id #Primary Key
        self.datetime = datetime
        self.dateweek = dateweek
        self.player_id = player_id
        self.current_club_id = current_club_id
        self.market_value = market_value
        self.player_club_domestic_competition_id = player_club_domestic_competition_id
        

    def add(self):
        query = "INSERT INTO PLAYERVALUATION (DATETIME, DATEWEEK, PLAYER_ID, CURRENT_CLUB_ID, MARKET_VALUE, PLAYER_CLUB_DOMESTIC_COMPETITION_ID) VALUES (?, ?, ?, ?, ?, ?)"
        tup = (self.player_valuation_id, self.datetime, self.dateweek, self.player_id, self.current_club_id, self.market_value, self.player_club_domestic_competition_id)
        return query, tup

    def update(self):
        query = "UPDATE PLAYERVALUATION SET DATETIME = ?, DATEWEEK = ?, PLAYER_ID = ?, CURRENT_CLUB_ID = ?, MARKET_VALUE = ?, PLAYER_CLUB_DOMESTIC_COMPETITION_ID = ? WHERE(PLAYER_VALUATION_ID = ?)"
        tup = (self.datetime, self.dateweek, self.player_id, self.current_club_id, self.market_value, self.player_club_domestic_competition_id, self.player_valuation_id)
        return query, tup

    def delete(self):
        query = "DELETE FROM PLAYERVALUATION WHERE (PLAYER_VALUATION_ID = ?)"
        return query, (self.player_valuation_id,)