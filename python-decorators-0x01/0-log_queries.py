import sqlite3
import functools
from datetime import datetime

### decorators to log SQL queries

""" YOUR CODE GOES HERE"""


def log_queries(fetch_all_user):
    def wrapper(*args, **kwargs):
        print('SQL query before execution')
        result = fetch_all_user(*args, **kwargs)
        print('SQL query after execution')
        return result
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users;")
