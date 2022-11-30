class Competition:
	def __init__(self, competition_id, pretty_name, type_, sub_type, country_id = -1, country_name = None, country_latitude = None, country_longitude = None, domestic_league_code = None, name = None, confederation = None, url = None):
		self.competition_id = competition_id
		self.pretty_name = pretty_name
		self.type_ = type_
		self.sub_type = sub_type
		self.country_id = country_id
		self.country_name = country_name
		self.country_latitude = country_latitude
		self.country_longitude = country_longitude
		self.domestic_league_code = domestic_league_code
		self.name = name
		self.confederation = confederation
		self.url = url

	def add(self):
		query = "INSERT INTO COMPETITION (COMPETITION_ID, PRETTY_NAME, TYPE_, SUB_TYPE, COUNTRY_ID, COUNTRY_NAME, COUNTRY_LATITUDE, COUNTRY_LONGITUDE, DOMESTIC_LEAGUE_CODE, NAME, CONFEDERATION, URL) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
		tupel = (self.competition_id, self.pretty_name, self.type_, self.sub_type, self.country_id, self.country_name, self.country_latitude, self.country_longitude, self.domestic_league_code, self.name, self.confederation, self.url)
		return query, tupel
	
	def update(self):
		query = "UPDATE COMPETITION SET PRETTY_NAME = ?, TYPE_ = ?, SUB_TYPE = ?, COUNTRY_ID = ?, COUNTRY_NAME = ?, COUNTRY_LATITUDE = ?, COUNTRY_LONGITUDE = ?, DOMESTIC_LEAGUE_CODE = ?, NAME = ?, CONFEDERATION = ?, URL = ? WHERE (COMPETITION_ID = ?)"
		tupel = (self.pretty_name, self.type_, self.sub_type, self.country_id, self.country_name, self.country_latitude, self.country_longitude, self.domestic_league_code, self.name, self.confederation, self.url, self.competition_id)
		return query, tupel
	
	def delete(self):
		query = "DELETE FROM COMPETITION WHERE (COMPETITION_ID = ?)"
		return query, (self.competition_id,)
