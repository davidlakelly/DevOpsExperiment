import sqlite3
connection = sqlite3.connect("DevOpsTest.db")
cursor = connection.cursor()


#Creating table for users
def create_table():
    query = "DROP TABLE IF EXISTS UserLogin"
    cursor.execute(query)
    conn.commit()
    query = "CREATE TABLE UserLogin(UserName text NOT NULL, PassWord text NOT NULL)"
    cursor.execute(query)
    conn.commit()
def enter(UserName, PassWord):
    query = "INSERT INTO UserLogin (UserName, PassWord) VALUES (USR1, PW1)"
    cursor.execute(query, (UserName, PassWord))
    conn.commit()


#Creating table for countries
def create_table():
    query = "DROP TABLE IF EXISTS Countries"
    cursor.execute(query)
    conn.commit()
    query = "CREATE TABLE Countries (Country VARCHAR, Year VARCHAR, change VARCHAR)"
    cursor.execute(query)
    conn.commit()
    query = "INSERT INTO UserLogin (UserName, PassWord) VALUES (USR1, PW1)"
    cursor.execute(query)
    conn.commit()


def select_all_tasks(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserLogin")

    rows = cur.fetchall()

    for row in rows:
        print(row)
