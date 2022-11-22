import psycopg2 as dbapi2

from club import Club

class Database:
    def __init__(self, dbfile):
        self.dbfile = dbfile  

    def add(self, object):
    	string, tupel = object.add()
    	with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string
            cursor.execute(query, tupel)
            connection.commit()

    def update(self, object):
    	string, tupel = object.update()
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string
            cursor.execute(query, tupel)
            connection.commit()

    def delete(self, object):
        string, object_id = object.delete()
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = string 
            cursor.execute(query, (object_id,))
            connection.commit()

    def get_club(self, club_id):
        with dbapi2.connect(self.dbfile) as connection:
            cursor = connection.cursor()
            query = "SELECT * FROM CLUB WHERE (CLUB_ID = ?)"
            cursor.execute(query, (club_id,))
            club_values = list(cursor.fetchone())
        club_ = Club(*club_values)
        return club_