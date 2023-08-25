from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()

book_genre_association = Table('book_genre', Base.metadata,
                               Column('book_id', Integer, ForeignKey('books.id')),
                               Column('genre_id', Integer, ForeignKey('genres.id'))
                               )

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", backref="author", cascade="all, delete-orphan")

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genres = relationship("Genre", secondary=book_genre_association, backref="books")
