class Admin:
    def __init__(self, student_id, name, mail, password):
        self.student_id = student_id
        self.name = name
        self.mail = mail
        self.password = password
        

    def add(self):
        query = "INSERT INTO ADMINS (STUDENT_ID, NAME, MAIL, PASSWORD) VALUES (?, ?, ?, ?)"
        tup = (self.student_id, self.name, self.mail, self.password)
        return query, tup

    def update(self):
        query = "UPDATE ADMINS SET NAME = ?, MAIL = ?, PASSWORD = ? WHERE(STUDENT_ID = ?)"
        tup = (self.student_id, self.name, self.mail)
        return query, tup

    def delete(self):
        query = "DELETE FROM ADMINS WHERE (STUDENT_ID = ?)"
        return query, (self.student_id,)