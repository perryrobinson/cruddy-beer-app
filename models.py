# models.py

from app import db
from sqlalchemy.orm import relationship, backref

class Brewery(db.Model):
    __tablename__ = "breweries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    beer_m = db.relationship('Beer', backref='breweries', lazy=True)

    def __repr__(self):
        return "<Brewery: {}="">".format(self.name)

class Beer(db.Model):
    __tablename__ = "beers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    abv = db.Column(db.Float)
    brewery_id =  db.Column(db.Integer, db.ForeignKey('breweries.id'), nullable='False')
