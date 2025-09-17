""" A generator script that fetches and processes data in batches from the users DB """

from seed import connect_to_prodev

connection = connect_to_prodev()

def stream_users_in_batches(batch_size):
    """ Fetches rows in batches"""
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user_data;')
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        for rows in batch:
            yield rows


def batch_processing(batch_size):
    """ Processes each batch to filter users over the age of 25 """
    pass