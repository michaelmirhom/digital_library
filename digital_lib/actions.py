from digital_lib.models import Author, Book, Genre
from sqlalchemy.exc import SQLAlchemyError
from digital_lib.database import Session
def create_author(name):
    session = Session()
    try:
        if not name:
            return "Author name cannot be empty!"
        existing_author = session.query(Author).filter_by(name=name).first()
        if existing_author:
            return f"Author {name} already exists!"
        author = Author(name=name)
        session.add(author)
        session.commit()
        print(f"Trying to add author: {name}")
        return f"Added author: {name}"
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
def list_authors():
    session = Session()
    authors_data = []  
    try:
        authors = session.query(Author).all()
        authors_data = [author.name for author in authors]
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"  
    finally:
        session.close()
    print(f"Listing authors: {authors_data}")
    return authors_data
def create_book(title, author_id, genre_names):
    session = Session()
    try:
        if not title:
            return "Book title cannot be empty!"
        existing_book = session.query(Book).filter_by(title=title).first()
        if existing_book:
            return f"Book {title} already exists!"
        
      
    
        