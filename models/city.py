#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String


class City(BaseModel, Base):
    """ A city in MySQL database
    Inherits from SQLAlchemy and links to the MySQL table cities

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Cities.
        name (sqlalchemy String): The name of the City.
        state_id (sqlalchemy String): The state id of the City.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"),nullable=False)
    name = Column(String(128), nullable=False)
