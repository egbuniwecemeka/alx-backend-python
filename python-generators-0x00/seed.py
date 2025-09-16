from mysql import connector
from mysql.connector import Error
from sys import argv
from csv import DictReader
from uuid import uuid4

def connect_db():
    """ Connects to a DB server """
    try:
        conn = connector.connect(
            host = 'localhost',
            user = argv[1],
            password = argv[2]
        )
        return conn
    except Error as e:
        print(f'Error {e}')
        return None

def create_database(connection):
    """ Creates a database ALX_prodev if it doesn't exist """
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS ALX_prodev;')
    cursor.close()

def connect_to_prodev():
    """ Connect to ALX_prodev DB """
    try:
        conn = connector.connect(
            host = 'localhost',
            user = argv[1],
            password = argv[2],
            database = 'ALX_prodev'
        )
        return conn
    except Error as e:
        print(f"Error {e}")
        return None

def create_table(connection):
    """ Creates a table user_data if not existing """
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY NOT NULL DEFAULT (UUID()),
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            age DECIMAL(10, 2) NOT NULL,
            INDEX(user_id)
        )
        """
    )
    cursor.close()

def insert_data(connection, data):
    """ Inserts data into user table from a csv file """
    cursor = connection.cursor()
    with open(data, newline='') as f:
        reader = DictReader(f)
        for row in reader:
            # Check if email exists to avoid duplcates
            cursor.execute("SELECT email FROM user_data WHERE email = %s", (row["email"],))
            if cursor.fetchone():
                continue
            query = """
                        INSERT INTO user_data (user_id, name, email, age)
                        VALUES (%s, %s, %s, %s);
                    """
            user_data = (str(uuid4()), row["name"], row["email"], float(row["age"]))
            try:
                cursor.execute(query, user_data)
            except Error as e:
                print(f"Insert values: {e}")
                connection.rollback()
    connection.commit()
    cursor.close()