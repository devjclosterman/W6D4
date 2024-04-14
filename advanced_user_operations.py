import sqlite3

class AdvancedUserOperations:
    def __init__(self):
        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()
        # self.cursor.execute(
        #   'Drop table if exists user'
        # )
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            password TEXT,
            age INTEGER,
            gender TEXT,
            address TEXT
        )''')
        self.conn.commit()
    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):
        self.cursor.execute(
            'INSERT INTO user (name, email, password, age, gender, address) VALUES (?, ?, ?, ?, ?, ?)',
            (name, email, password, age, gender, address)
        )
        self.conn.commit()
        return "Created a new record with ID: "+str(self.cursor.lastrowid)
    
    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):
        sql = 'SELECT * FROM user WHERE age >= ? AND age <= ? AND gender = ?'
        self.cursor.execute(sql, 
            (min_age, max_age, gender)
        )
        results = self.cursor.fetchall()
        # print(self.cursor.execute("SELECT * FROM user"))
        print(self.cursor.execute("SELECT * FROM user").fetchall())
        return results
    def update_user_profile(self, email, age=None, gender=None, address=None):
        affected_rows = self.cursor.execute(
            'UPDATE user SET age=?, gender=?, address=? WHERE email=?',
            (age, gender, address, email)
        )
        self.conn.commit()
        return "Updated "+str(affected_rows.rowcount) + " Row(s)"
    
    def delete_users_by_criteria(self, gender=None):
        pass
    def __del__(self):
        self.conn.close()

