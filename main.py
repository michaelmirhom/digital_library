import click
from digital_lib.actions import create_author, create_book, list_books, list_authors, update_book, delete_book, search_books
from digital_lib.database import init_db
def author_menu():
     choice = click.prompt("Enter the number of your choice", type=str)
     while True:
        click.echo("======== Author Menu ========")
        click.echo("1. Add Author")
        click.echo("2. List Authors")
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