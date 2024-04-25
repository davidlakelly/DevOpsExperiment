import flask
import psycopg2

conn = psycopg2.connect(database = "DevopsExp", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "password",
                        port = 5432)




cur = conn.cursor()
# Execute a command: create user table
cur.execute("""CREATE TABLE user(
            User_id SERIAL PRIMARY KEY,
            User VARCHAR (50) UNIQUE NOT NULL,
            Pass VARCHAR (20) NOT NULL);
            """)

conn.commit()
'''
cur.close()

#conn.close()


cur.execute("INSERT INTO datacamp_courses(User_id, User, Pass) VALUES('01','Test','Password1$')");


conn.commit()
cur.close()
conn.close()


cur = conn.cursor()
cur.execute('SELECT * FROM user;')
rows = cur.fetchall()
conn.commit()
conn.close()
for row in rows:
    print(row)

'''