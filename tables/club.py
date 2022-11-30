class Club:
	def __init__(self, club_id, name, pretty_name, domestic_competition_id, total_market_value = None, squad_size = None, average_age = None, foreigners_number = None, foreigners_percentage = None, national_team_players = None, stadium_name = None, stadium_seats = None, net_transfer_record = None, coach_name = None, url = None):
		self.club_id = club_id
		self.name = name
		self.pretty_name = pretty_name
		self.domestic_competition_id = domestic_competition_id
		self.total_market_value = total_market_value
		self.squad_size = squad_size
		self.average_age = average_age
		self.foreigners_number = foreigners_number
		self.foreigners_percentage = foreigners_percentage
		self.national_team_players = national_team_players
		self.stadium_name = stadium_name
		self.stadium_seats = stadium_seats
		self.net_transfer_record = net_transfer_record
		self.coach_name = coach_name
		self.url = url

	def add(self):
		query = "INSERT INTO CLUB (CLUB_ID, NAME, PRETTY_NAME, DOMESTIC_COMPETITION_ID, TOTAL_MARKET_VALUE, SQUAD_SIZE, AVERAGE_AGE, FOREIGNERS_NUMBER, FOREIGNERS_PERCENTAGE, NATIONAL_TEAM_PLAYERS, STADIUM_NAME, STADIUM_SEATS, NET_TRANSFER_RECORD, COACH_NAME, URL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
		tupel = (self.club_id, self.name, self.pretty_name, self.domestic_competition_id, self.total_market_value, self.squad_size, self.average_age, self.foreigners_number, self.foreigners_percentage, self.national_team_players, self.stadium_name, self.stadium_seats, self.net_transfer_record, self.coach_name, self.url)
		return query, tupel
	
	def update(self):
		query = "UPDATE CLUB SET NAME = ?, PRETTY_NAME = ?, DOMESTIC_COMPETITION_ID = ?, TOTAL_MARKET_VALUE = ?, SQUAD_SIZE = ?, AVERAGE_AGE = ?, FOREIGNERS_NUMBER = ?, FOREIGNERS_PERCENTAGE = ?, NATIONAL_TEAM_PLAYERS = ?, STADIUM_NAME = ?, STADIUM_SEATS = ?, NET_TRANSFER_RECORD = ?, COACH_NAME = ?, URL = ? WHERE (CLUB_ID = ?)"
		tupel = (self.name, self.pretty_name, self.domestic_competition_id, self.total_market_value, self.squad_size, self.average_age, self.foreigners_number, self.foreigners_percentage, self.national_team_players, self.stadium_name, self.stadium_seats, self.net_transfer_record, self.coach_name, self.url, self.club_id)
		return query, tupel
	
	def delete(self):
		query = "DELETE FROM CLUB WHERE (CLUB_ID = ?)"
		return query, (self.club_id,)
