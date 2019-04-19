from orm import CustomIntegrityError
import config
import socket
import migrations
import orm
import menu
from datetime import datetime


def validate_user(connection, data):
    try:
        user = orm.get_user_by_card_id(card_id=data)
        if user:
            connection.sendall(config.SERVER_SUCCESS_RESPONSE)
        else:
            connection.sendall(config.SERVER_ERROR_RESPONSE)
            user = 'Not Found'
        now = datetime.now().strftime(config.DATETIME_FORMAT)
        print(config.LOG_PATTERN.format(h=config.HOST, p=config.PORT, m=data, u=user, d=now))
    except Exception as e:
        connection.sendall(config.SERVER_ERROR_RESPONSE)
        print('Error: {}'.format(e))


def add_user(connection, data, name, last_name):
    try:
        orm.insert_user(
            name=name,
            last_name=last_name,
            card_id=data
        )
        user = orm.get_user_by_card_id(card_id=data)
        connection.sendall(config.SERVER_SUCCESS_RESPONSE)
        print(config.LOG_PATTERN.format(h=config.HOST, p=config.PORT, m=data, u=user))
        print('Success! user created: {}'.format(user))
        raise KeyboardInterrupt
    except CustomIntegrityError as e:
        connection.sendall(config.SERVER_ERROR_RESPONSE)
        user = orm.get_user_by_card_id(card_id=data)
        print('User founded: {}'.format(user))
        print(e.msg)
    except Exception as e:
        connection.sendall(config.SERVER_ERROR_RESPONSE)
        print('Error: {}'.format(e))


def tcp_loop(function, **kwargs):
    try:
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((config.HOST, config.PORT))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        function(connection=conn, data=data, **kwargs)
    except KeyboardInterrupt:
        print(config.SERVER_END_MSG)


def validate_user_action():
    print(menu.MENU_OPTIONS['1']['log_pattern'].format(h=config.HOST, p=config.PORT))
    tcp_loop(validate_user)


def add_user_action():
    print(menu.MENU_OPTIONS['2']['title'])
    name = input(menu.MENU_OPTIONS['2']['items']['name'])
    last_name = input(menu.MENU_OPTIONS['2']['items']['last_name'])
    input(menu.MENU_OPTIONS['2']['items']['ready'])
    print(menu.MENU_OPTIONS['2']['log_pattern'].format(h=config.HOST, p=config.PORT))
    kwargs = {
        'name': name,
        'last_name': last_name,
    }
    tcp_loop(function=add_user, **kwargs)


def run_migrations_action():
    print(menu.MENU_OPTIONS['3']['title'])
    confirmation = input(menu.MENU_OPTIONS['3']['confirmation'])
    if str(confirmation).upper() == 'Y':
        try:
            migrations.insert_users()
            print(menu.MENU_OPTIONS['3']['ready'])
        except CustomIntegrityError as e:
            print(e.msg)
    else:
        print(menu.MENU_OPTIONS['3']['cancel'])


def reset_and_create_schemas_action():
    print(menu.MENU_OPTIONS['4']['title'])
    confirmation = input(menu.MENU_OPTIONS['4']['confirmation'])
    if str(confirmation).upper() == 'Y':
        migrations.reset_and_create_schemas()
        print(menu.MENU_OPTIONS['4']['ready'])
    else:
        print(menu.MENU_OPTIONS['4']['cancel'])
