import click
from digital_lib.actions import create_author, create_book, list_books, list_authors, update_book, delete_book, search_books
from digital_lib.database import init_db


def author_menu():
    while True:
        click.echo("======== Author Menu ========")
        click.echo("1. Add Author")
        click.echo("2. List Authors")
        click.echo("3. Delete Author")
        click.echo("3. Go Back to Main Menu")
        choice = click.prompt("Enter the number of your choice", type=str)

        if choice == "1":
            name = click.prompt("Enter the name of the author")
            result = create_author(name)
            click.echo(result)
        elif choice == "2":
            authors = list_authors()
            for author in authors:
                click.echo(author)
        elif choice == "3":
            break
        else:
            click.echo("Invalid choice, please try again.")
def book_menu():
    while True:
        click.echo("======== Book Menu ========")
        click.echo("1. Add Book")
        click.echo("2. List Books")
        click.echo("3. Update Book")
        click.echo("4. Delete Book")
        click.echo("5. Search Books")
        click.echo("6. Go Back to Main Menu")
        choice = click.prompt("Enter the number of your choice", type=str)
        if choice == "1":
          title = click.prompt("Enter the title of the book")
          author_id = click.prompt("Enter the ID of the author", type=int)
          genre_names = [g.strip() for g in click.prompt("Enter genre names (comma separated)", type=str).split(',')]
          result = create_book(title, author_id, genre_names)
          click.echo(result)
        elif choice == "2":
            books = list_books()
            for book in books:
                click.echo(f"{book['title']} by {book['author']}. Genres: {', '.join(book['genres'])}")
        elif choice == "3":
            book_id = click.prompt("Enter the ID of the book to update", type=int)
            new_title = click.prompt("Enter the new title (or hit Enter to skip)", default="")
            new_author_id = click.prompt("Enter the new author ID (or hit Enter to skip)", default="")
            new_genre_ids = click.prompt("Enter the new genre IDs (comma separated, or hit Enter to skip)", default="").split(',')
            result = update_book(book_id, new_title, new_author_id, new_genre_ids)
            click.echo(result)
        elif choice == "4":
            book_id = click.prompt("Enter the ID of the book to delete", type=int)
            result = delete_book(book_id)
            click.echo(result)
        elif choice == "5":
            search_term = click.prompt("Enter the search term")
            books = search_books(search_term)
            for book in books:
                click.echo(f"{book['title']} by {book['author']}. Genres: {', '.join(book['genres'])}")
        elif choice == "6":
            break
        else:
            click.echo("Invalid choice, please try again.")


@click.command()
def main_menu():
    while True:
        click.echo("======== Digital Library Menu ========")
        click.echo("1. Author")
        click.echo("2. Book")
        click.echo("3. Exit")
        choice = click.prompt("Enter the number of your choice", type=str)

        if choice == "1":
            author_menu()
        elif choice == "2":
            book_menu()
        elif choice == "3":
            click.echo("Goodbye! Thanks for using Digital Library!")
            break
        else:
            click.echo("Invalid choice, please try again.")          
if __name__ == "__main__":
    init_db()
    print("Database initialized!")
    main_menu()

            



