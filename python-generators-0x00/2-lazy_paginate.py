from seed import connect_to_prodev

def paginate_users(page_size, offset):
    """ A generator function that fetches rows from a DB table"""
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f'SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}')
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """ Fetch the next page when needed at offset 0 """
    offset = 0
    rows = paginate_users(page_size, offset)
    for row in rows:
        if not row:
            break
        yield row
    offset += page_size
