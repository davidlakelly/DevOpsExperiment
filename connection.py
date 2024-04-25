Import flask
Import psycopg2

conn = psycopg2.connect(database = "DevopsExp", 
                        user = "User", 
                        host= 'localhost',
                        password = "Password",
                        port = 5432)