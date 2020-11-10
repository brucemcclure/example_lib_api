# 99% of the time you want a model for each table in the db. 
from main import db #db connection

class Book(db.Model):
    __tablename__ = "books" # declaring the name of the table in the db
    # The name of the attribute maps to the name of the column on the table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())