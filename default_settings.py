import os  # This is the OS package which is used to retrieve environment variables


#connect to postgres+using psycopg2://username:password@localhost:port/name_of_db 
class Config(object):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://app:{os.getenv('DB_PASSWORD')}@localhost:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # If not needed then this should be disabled because it uses extra memory.


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()