from db import get_connection


def get_user_by_id(user_id):
    # Get a cursor object
    CONN = get_connection()
    cursor = CONN.cursor()
    # query
    cursor.execute(
        '''SELECT name, email, phone FROM users WHERE id=?''',
        (user_id,)
    )
    user = cursor.fetchone()
    CONN.close()

    return user


def get_user_by_card_id(card_id):
    # Get a cursor object
    CONN = get_connection()
    cursor = CONN.cursor()
    # query
    cursor.execute(
        '''SELECT * FROM users WHERE card_id like ?''',
        (card_id,)
    )
    user = cursor.fetchone()
    CONN.close()

    return user


def update_user(card_id, name, last_name):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # query
        cursor.execute(
            '''UPDATE users SET name = ?, last_name = ? WHERE card_id = ? ''',
            (name, last_name, card_id)
        )
        # Commit the change
        CONN.commit()
    # Catch the exception
    except Exception as e:
        # Roll back any change if something goes wrong
        CONN.rollback()
        raise e
    finally:
        # Close the db connection
        CONN.close()


def delete_user_by_card_id(card_id):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # query
        cursor.execute('''DELETE FROM users WHERE card_id = ? ''', (card_id,))
        # Commit the change
        CONN.commit()
    # Catch the exception
    except Exception as e:
        # Roll back any change if something goes wrong
        CONN.rollback()
        raise e
    finally:
        # Close the db connection
        CONN.close()


def insert_user(name, last_name, card_id):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # Insert user 1
        cursor.execute('''
            INSERT INTO users(name, last_name, card_id) VALUES(?,?,?)''',
                       (name, last_name, card_id)
                       )
        # Commit the change
        CONN.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        CONN.rollback()
        raise e
    finally:
        # Close the db connection
        CONN.close()
