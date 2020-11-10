from flask_sqlalchemy import SQLAlchemy    # This is the package for the orm
import os                               # This is the OS package which is used to retrieve environment variables



def init_db(app): # Method to initialize db
    #connect to postgres+using psycopg2://username:password@localhost:port/name_of_db 
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://app:{os.getenv('DB_PASSWORD')}@localhost:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # If not needed then this should be disabled because it uses extra memory. 
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