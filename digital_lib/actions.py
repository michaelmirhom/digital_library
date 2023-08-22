from digital_lib.models import Author, Book, Genre
from sqlalchemy.exc import SQLAlchemyError
from digital_lib.database import Session
def create_author(name):
    session = Session()
    try:
        if not name:
            return "Author name cannot be empty!"
        existing_author = session.query(Author).filter_by(name=name)
        if existing_author:
            return f"Author {name} already exists!"
        