from db import get_connection
import orm


def create_user_table():
    CONN = get_connection()
    cursor = CONN.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')
    cursor.execute('''
        CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                           phone TEXT, email TEXT unique, password TEXT)
    ''')
    CONN.commit()
    CONN.close()


create_user_table()

orm.insert_user(
    name='Cristian',
    phone=1234,
    email='test@gmail.com',
    password=1234
)

print(orm.get_user_by_name(name='Cristian'))
