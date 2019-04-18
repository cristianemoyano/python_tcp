from db import get_connection
import orm


def create_user_table():
    try:
        CONN = get_connection()
        cursor = CONN.cursor()
        cursor.execute('''
            DROP TABLE IF EXISTS users;
        ''')
        cursor.execute('''
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                               last_name TEXT, card_id TEXT unique)
        ''')
        cursor.execute('''
            CREATE INDEX card_id_number ON users (card_id);
        ''')
        CONN.commit()
    except Exception:
        pass
    finally:
        # Close the db connection
        CONN.close()


create_user_table()

orm.insert_user(
    name='Cristian',
    last_name='Moyano',
    card_id='ASF1235',
)
