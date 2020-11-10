import psycopg2
import os

connection = psycopg2.connect(
    database="library_api",
    user="app",
    password=os.getenv("DB_PASSWORD"),
    host="localhost"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()