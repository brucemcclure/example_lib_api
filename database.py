from flask_sqlalchemy import SQLAlchemy # This is the package for the orm



def init_db(app): # Method to initialize db
    db = SQLAlchemy(app) # Create a db object from the alchemy class with app as the argument
    return db  




# import psycopg2                 # This is the package to connect to postgres
# import os                       # This is the OS package which is used to retrieve environment variables

# connection = psycopg2.connect(  # These are the db connection config
#     database="library_api",
#     user="app",
#     password=os.getenv("DB_PASSWORD"),
#     host="localhost"
# )

# cursor = connection.cursor()  # Creating the cursor

# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);") # Creats the DB table if it doesnt already exist
# connection.commit() # Commits the transaction