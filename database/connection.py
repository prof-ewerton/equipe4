import sqlite3

def get_db_connection():
    connection = sqlite3.connect("sistema.db")
    return connection