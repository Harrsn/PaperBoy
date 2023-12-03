# Import necessary libraries
import sqlite3
from sqlite3 import Error
import logging

# Configure logging with ERROR level
logging.basicConfig(level=logging.ERROR)

def connect():
    # Attempt to establish a connection to the SQLite database
    try:
        conn = sqlite3.connect('content.db')
        # SQL statement to create content_agg table if it doesn't exist
        sql_create_projects_table = "CREATE TABLE IF NOT EXISTS content_agg (source TEXT NOT NULL, title TEXT NOT NULL, url TEXT NOT NULL, CONSTRAINT PK PRIMARY KEY(source, title, url));"
        if conn is not None:
            # Create the table if the connection is successful
            create_table(conn, sql_create_projects_table)
            return conn
        else:
            # Log an error if the connection cannot be established
            logging.error("Error! Cannot create the database connection.")
            return None
    except Error as e:
        # Log an error if there is an issue during connection setup
        logging.error(e)
        return None

def create_table(conn, create_table_sql):
    # Attempt to create the content_agg table
    try:
        with conn:
            c = conn.cursor()
            c.execute(create_table_sql)
    except Error as e:
        # Log an error if there is an issue creating the table
        logging.error("Error: %s", e)

# Usage example
if __name__ == "__main__":
    # Attempt to establish a database connection
    connection = connect()

    # Print a message based on the success of the connection attempt
    if connection:
        print("Database connection established.")
    else:
        print("Failed to establish a database connection.")
