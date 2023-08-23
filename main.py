import click
from digital_lib.actions import create_author, create_book, list_books, list_authors, update_book, delete_book, search_books
from digital_lib.database import init_db
