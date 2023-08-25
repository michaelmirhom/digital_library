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
        author = session.query(Author).filter_by(id=author_id).first()
        if not author:
            return f"Author with ID {author_id} does not exist!"
        genres = []
        for genre_name in genre_names:
            genre = session.query(Genre).filter_by(name=genre_name).first()
            if not genre:
                genre = Genre(name=genre_name)
                session.add(genre)
            genres.append(genre)
        book = Book(title=title, author_id=author_id)
        book.genres = genres
        session.add(book)
        session.commit()
        return f"Added book: {title} with genres: {', '.join(genre_names)}"    
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
def list_genres():
    session = Session()
    genre_data = []  
    try:
        genres = session.query(Genre).all()
        genre_data = [{"id": genre.id, "name": genre.name} for genre in genres]
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
    return genre_data
def list_books(author_id=None):
    session = Session()
    books_data = []
    try:
        if author_id is None:
            books = session.query(Book).all()
        else:
            author = session.query(Author).filter_by(id=author_id).first()
            if not author:
                return f"Author with ID {author_id} does not exist!"
            books = session.query(Book).filter(Book.author_id == author_id).all()
            books_data = [
            {
                "title": book.title,
                "author": book.author.name,
                "genres": [genre.name for genre in book.genres]
            }
            for book in books
        ]
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"  
    finally:
        session.close()

    return books_data  
def update_book(book_id, new_title=None, new_author_id=None, new_genre_names=None):
    session = Session()
    try:
        book = session.query(Book).filter_by(id=book_id).first()
        if not book:
            return f"Book with ID {book_id} does not exist!"
        if new_title:
            book.title = new_title
        if new_author_id:
            author = session.query(Author).filter_by(id=new_author_id).first()
            if not author:
                return f"Author with ID {new_author_id} does not exist!"
            book.author_id = new_author_id
        
        if new_genre_names:
            genres = []
            for genre_name in new_genre_names:
                genre = session.query(Genre).filter_by(name=genre_name).first()
                if not genre:
                    genre = Genre(name=genre_name)
                    session.add(genre)
                genres.append(genre)
            book.genres = genres  
        session.commit()
        return f"Updated book with ID {book_id} successfully!" 
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"  
    finally:
        session.close()
def delete_book(book_id):
    session = Session()  
    try:
        book = session.query(Book).filter_by(id=book_id).first()
        if not book:
            return f"Book with ID {book_id} does not exist!" 
        session.delete(book)
        session.commit()
        return f"Deleted book with ID {book_id} successfully!"
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
def search_books(search_term):
    session = Session()
    results = []
    try:
        books = session.query(Book).filter(Book.title.contains(search_term)).all()
        results = [{"title": book.title, "author": book.author.name, "genres": [genre.name for genre in book.genres]} for book in books]
    except SQLAlchemyError as e:
        return f"An error occurred: {str(e)}"
    finally:
        session.close()
      
    return results  
  

        
      
    
        