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


def get_user_by_name(name):
    # Get a cursor object
    CONN = get_connection()
    cursor = CONN.cursor()
    # query
    cursor.execute(
        '''SELECT name, email, phone FROM users WHERE name like ?''',
        (name,)
    )
    user = cursor.fetchone()
    CONN.close()

    return user


def update_user(user_id, phone):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # query
        cursor.execute(
            '''UPDATE users SET phone = ? WHERE id = ? ''',
            (phone, user_id)
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


def delete_user(user_id, phone):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # query
        cursor.execute('''DELETE FROM users WHERE id = ? ''', (user_id,))
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


def insert_user(name, phone, email, password):
    try:
        # Get a cursor object
        CONN = get_connection()
        cursor = CONN.cursor()
        # Insert user 1
        cursor.execute('''
            INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''',
                       (name, phone, email, password)
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
