# Digital Library

Welcome to the Digital Library project. This CLI application allows you to manage a collection of books, their authors, and associated genres.

# Description

This application provides a menu-driven interface, using which you can perform CRUD operations for both authors and books. It helps you maintain your digital collection of books efficiently.

# Installation

Follow these steps to set up the Digital Library:
1- First, clone the repository:
git clone <git@github.com>:michaelmirhom/digital_library.git

2- Navigate to the directory:
cd digital_library

3-Set up a virtual environment:
pip install pipenv
pipenv shell

4- Install the necessary dependencies:
pipenv install click sqlalchemy

# How to Use

To use the Digital Library, run the following command:
python main.py
You will be greeted with the main menu, offering you various options related to authors and books. Simply follow the on-screen prompts to navigate through the app. There are functions to add books, list all books, update book details, delete books, and search for books. Similarly, for authors, you can add, list, or delete them.

# File Descriptions

1-main.py: This is the entry point of the application. It houses the main menu and is responsible for user interactions.
2-actions.py: Contains all the core functionalities and operations, such as creating authors, updating books, and so on.
3-models.py: Defines the database models, i.e., the Author, Book, and Genre tables and their relationships.
4-database.py: Manages database connections and initializations.

# Contributor's Guide

 If you wish to contribute:
1-Fork the repository.
2-Create a new branch.
3-Make changes or additions.
4-Create a pull request.

# License
  
  This project is licensed under the MIT License.
