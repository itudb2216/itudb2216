import psycopg2 as dbapi2


class Player:
    def __init__(self,player_id,pretty_name,club_id,club_pretty_name,current_club_id,country_of_citizenship,country_of_birth = None, date_of_birth = None,
            position = None,sub_position = None,name = None,foot = None,height_in_cm = None,market_value_in_gbp = None,highest_market_value_in_gbp = None,agent_name = None,contract_expiration_date = None,
            domestic_competition_id = None,club_name = None,image_url = None,last_season = None,url = None):
        self.player_id = player_id
        self.pretty_name = pretty_name
        self.club_id = club_id
        self.club_pretty_name = club_pretty_name
        self.current_club_id = current_club_id
        self.country_of_citizenship = country_of_citizenship
        self.country_of_birth = country_of_birth
        self.date_of_birth = date_of_birth
        self.position = position
        self.sub_position = sub_position
        self.name = name
        self.foot = foot
        self.height_in_cm = height_in_cm
        self.market_value_in_gbp = market_value_in_gbp
        self.highest_market_value_in_gbp = highest_market_value_in_gbp
        self.agent_name = agent_name
        self.contract_expiration_date = contract_expiration_date
        self.domestic_competition_id = domestic_competition_id
        self.club_name = club_name
        self.image_url = image_url
        self.last_season = last_season
        self.url = url

    def add(self):
        query = "INSERT INTO PLAYERS VALUE(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        v = (self.player_id,self.pretty_name,self.club_id,self.club_pretty_name,self.current_club_id,self.country_of_citizenship,self.country_of_birth,self.date_of_birth,self.position,self.sub_position,self.name,self.foot,self.height_in_cm,self.market_value_in_gbp,self.highest_market_value_in_gbp,self.agent_name,self.contract_expiration_date,self.domestic_competition_id,self.club_name,self.image_url,self.last_season,self.url)
        return query, v

    def update(self):
        query = "UPDATE PLAYERS SET pretty_name = ?,club_id = ?,club_pretty_name = ?,current_club_id = ?,country_of_citizenship = ?,country_of_birth = ?,date_of_birth = ?,position = ?,sub_position = ?,name = ?,foot,height_in_cm = ?,market_value_in_gbp = ?,highest_market_value_in_gbp = ?,agent_name = ?,contract_expiration_date = ?,domestic_competition_id = ?,club_name = ?,image_url = ?,last_season = ?,url = ? WHERE (player_id = ?)"
        v = (self.pretty_name,self.club_id,self.club_pretty_name,self.current_club_id,self.country_of_citizenship,self.country_of_birth,self.date_of_birth,self.position,self.sub_position,self.name,self.foot,self.height_in_cm,self.market_value_in_gbp,self.highest_market_value_in_gbp,self.agent_name,self.contract_expiration_date,self.domestic_competition_id,self.club_name,self.image_url,self.last_season,self.url,self.player_id)
        return query, v
    
    def delete(self):
        query = "DELETE FROM PLAYERS WHERE (players_id = ?)"
        return query, (self.player_id,)
    