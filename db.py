import sqlite3


def get_connection():
    # Creates or opens a file called database with a SQLite3 DB
    return sqlite3.connect('database')
