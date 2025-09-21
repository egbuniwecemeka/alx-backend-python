import sqlite3
import functools
from datetime import datetime

### decorators to log SQL queries

""" YOUR CODE GOES HERE"""


def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'[{datetime.now()}] SQL query before execution')
        result = func(*args, **kwargs)
        print(f'[{datetime.now()}] SQL query after execution')
        return result
    return wrapper

""" My code ends here"""

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
