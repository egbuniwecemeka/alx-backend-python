""" Generator script that streams rows from an SQL database one by one """

from seed import connect_to_prodev, Error

def stream_users():
    ''' Retrieves rows from a table one after the other '''
    conn = connect_to_prodev()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:
            yield row
    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        conn.close()