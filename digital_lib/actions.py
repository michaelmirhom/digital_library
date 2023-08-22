from digital_lib.models import Author, Book, Genre
from sqlalchemy.exc import SQLAlchemyError
from digital_lib.database import Session
def create_author(name):
    session = Session()