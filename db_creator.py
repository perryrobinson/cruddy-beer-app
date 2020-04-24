# db_creator.py

import sqlalchemy
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///beer.db', echo=True)
Base = declarative_base()

class Brewery(Base):
    __tablename__ = 'breweries'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    state = Column(String)

    brewery_children = relationship('Beer', back_populates='breweries')

class Beer(Base):
    __tablename__ = 'beers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    abv = Column(Float)

    brewery_id = Column(Integer, ForeignKey('breweries.id'))
    brewery = relationship('Brewery', back_populates='brewery_children')

# create tables
Base.metadata.create_all(engine)
