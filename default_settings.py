import os  # This is the OS package which is used to retrieve environment variables

# Parent class called config. All other classes inherit from it.
class Config(object):                                   
    #connect to postgres+using psycopg2://username:password@localhost:port/name_of_db 
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://app:{os.getenv('DB_PASSWORD')}@localhost:5432/library_api"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # If not needed then this should be disabled because it uses extra memory.


class DevelopmentConfig(Config): # Inherits from config
    DEBUG = True

class ProductionConfig(Config): # Inherits from config
    pass

class TestingConfig(Config): # Inherits from config
    TESTING = True

environment = os.environ.get("FLASK_ENV") # Retrieve the the flask env variable

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()