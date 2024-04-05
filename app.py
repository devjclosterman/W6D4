import sqlite3

# Database Setup
def setup_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Create user table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        age INTEGER,
                        gender TEXT,
                        address TEXT
                    )''')
    conn.commit()
    conn.close()

# Migration Script
def migrate_database():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    # Add additional fields to the existing user table
    cursor.execute('''ALTER TABLE users
                      ADD COLUMN age INTEGER,
                      ADD COLUMN gender TEXT,
                      ADD COLUMN address TEXT''')
    conn.commit()
    conn.close()

# CRUD Operations Implementation
def create_user_with_profile(username, age, gender, address):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO users (username, age, gender, address)
                      VALUES (?, ?, ?, ?)''', (username, age, gender, address))
    user_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return user_id

def retrieve_users_by_criteria(criteria):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    query = '''SELECT * FROM users WHERE {}'''.format(criteria)
    cursor.execute(query)
    users = cursor.fetchall()

    conn.close()
    return users

def update_user_profile(user_id, age=None, gender=None, address=None):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    updates = []
    if age is not None:
        updates.append(('age', age))
    if gender is not None:
        updates.append(('gender', gender))
    if address is not None:
        updates.append(('address', address))

    update_query = ', '.join(['{} = ?'.format(field) for field, _ in updates])
    values = [value for _, value in updates]
    
    query = '''UPDATE users SET {} WHERE id = ?'''.format(update_query)
    cursor.execute(query, values + [user_id])

    conn.commit()
    conn.close()

def delete_users_by_criteria(criteria):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    query = '''DELETE FROM users WHERE {}'''.format(criteria)
    cursor.execute(query)

    conn.commit()
    conn.close()

# Unit Testing (Example)
def test_create_user_with_profile():
    user_id = create_user_with_profile('John', 30, 'Male', '123 Street, City')
    assert user_id is not None

def test_retrieve_users_by_criteria():
    users = retrieve_users_by_criteria("age > 25 AND gender = 'Male'")
    assert len(users) > 0

def test_update_user_profile():
    update_user_profile(1, age=35, address='456 Avenue, Town')
    user = retrieve_users_by_criteria("id = 1")[0]
    assert user[2] == 35 and user[4] == '456 Avenue, Town'

def test_delete_users_by_criteria():
    delete_users_by_criteria("gender = 'Male'")
    users = retrieve_users_by_criteria("gender = 'Male'")
    assert len(users) == 0

if __name__ == "__main__":
    setup_database()
    migrate_database()

    # Run unit tests
    test_create_user_with_profile()
    test_retrieve_users_by_criteria()
    test_update_user_profile()
    test_delete_users_by_criteria()
    print("All tests passed successfully.")
