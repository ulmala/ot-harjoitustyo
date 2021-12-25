import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_db_connection():
    """Returns the database connection to the default database configure above.

    Returns:
        sqlite3.connection: connection to the database
    """
    return connection