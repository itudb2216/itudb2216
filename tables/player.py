
class Player:
    def __init__(self,player_id,pretty_name,club_id,club_pretty_name,current_club_id,country_of_citizenship, date_of_birth = None,
            position = None,foot = None,height_in_cm = None,market_value_in_gbp = None,highest_market_value_in_gbp = None):
        self.player_id = player_id
        self.pretty_name = pretty_name
        self.club_id = club_id
        self.club_pretty_name = club_pretty_name
        self.current_club_id = current_club_id
        self.country_of_citizenship = country_of_citizenship
        self.date_of_birth = date_of_birth
        self.position = position
        self.foot = foot
        self.height_in_cm = height_in_cm
        self.market_value_in_gbp = market_value_in_gbp
        self.highest_market_value_in_gbp = highest_market_value_in_gbp
 

    def add(self):
        query = "INSERT INTO PLAYERS VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        v = (self.player_id,self.pretty_name,self.club_id,self.club_pretty_name,self.current_club_id,self.country_of_citizenship,self.date_of_birth,self.position,self.foot,self.height_in_cm,self.market_value_in_gbp,self.highest_market_value_in_gbp)
        return query, v

    def update(self):
        query = "UPDATE PLAYERS SET pretty_name = ?,club_id = ?,club_pretty_name = ?,current_club_id = ?,country_of_citizenship = ?,date_of_birth = ?,position = ?,foot = ?,height_in_cm = ?,market_value_in_gbp = ?,highest_market_value_in_gbp = ? WHERE (player_id = ?)"
        v = (self.pretty_name,self.club_id,self.club_pretty_name,self.current_club_id,self.country_of_citizenship,self.date_of_birth,self.position,self.foot,self.height_in_cm,self.market_value_in_gbp,self.highest_market_value_in_gbp,self.player_id)
        return query, v
    
    def delete(self):
        query = "DELETE FROM PLAYERS WHERE (players_id = ?)"
        return query, (self.player_id,)
    