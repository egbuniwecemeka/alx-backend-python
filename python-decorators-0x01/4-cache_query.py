import sqlite3
import functools

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        connect = sqlite3.connect('users.db')
        connect_db = func(connect, *args, **kwargs)
        connect.close()
        return connect_db
    return wrapper

def cache_query(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            key = (func.__name__, args, kwargs)
            if key in cache:
                return cache[key]
            else:
                result = func(conn, *args, **kwargs)
                cache[key] = result
        except Exception as e:
            return e        

@with_db_connection
@cache_query

def get_users_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM users WHERE id= ?;', (user_id,))
    data = cursor.fetchall()
    return data
