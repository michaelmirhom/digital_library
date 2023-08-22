from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    

    id = Column(Integer, primary_key=True)
    name = Column(String)
class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String)
   