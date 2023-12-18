#!/usr/bin/python3
"""Connects to the table city using sqlalchemy"""


import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base
from sqlalchemy import ForeignKey


class City(Base):
    """Defines the table city"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
