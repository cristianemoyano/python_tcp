
import socket
import orm
from orm import CustomIntegrityError
import config
import migrations


MENU_START_MSG = 'Please select an option: '

MENU_OPTIONS = {
    '1': {
        'value': 1,
        'label': 'Validate users',
        'log_pattern': "-- Mode: Validate users - App listen on: {h}:{p} ---",
    },
    '2': {
        'title': "-- Mode: Add users --",
        'value': 2,
        'label': 'Add users',
        'items': {
            'name': 'Please, enter the first name: ',
            'last_name': 'Now enter the last name: ',
            'ready': "Finally, prepare the card. Are you ready? Enter any key when you're ready."
        },
        'log_pattern': "-- Mode: Add users - App listen on: {h}:{p} ---",
    },
    '3': {
        'title': "-- Mode: Run migrations --",
        'value': 3,
        'label': 'Run migrations',
        'confirmation': 'Do you really want to run the migrations? Y / N: ',
        'ready': 'Migrations successfully run.',
        'cancel': 'Migrations cancelled.'
    },
    '4': {
        'title': "-- Mode: Reset and create schemas --",
        'value': 4,
        'label': 'Reset and create schemas',
        'confirmation': 'Do you really want to reset the database? Y / N: ',
        'ready': 'Database successfully reseted.',
        'cancel': 'Script cancelled.'
    },
    '5': {
        'value': 5,
        'label': 'Exit',
    },
}


def generate_option_labels():
    j = ' \n '
    d = '.'
    s = ' '
    options = "Options: " + j
    for key, opt in MENU_OPTIONS.items():
        options += key + d + s + opt.get('label') + j
    return options


def validate_user(connection, data):
    try:
        user = orm.get_user_by_card_id(card_id=data)
        if user:
            connection.sendall(config.SERVER_SUCCESS_RESPONSE)
        else:
            connection.sendall(config.SERVER_ERROR_RESPONSE)
            user = 'Not Found'
        print(config.LOG_PATTERN.format(h=config.HOST, p=config.PORT, m=data, u=user))
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


def main():
    print(config.SERVER_START_MSG)
    print(generate_option_labels())
    option_selected = input(MENU_START_MSG)
    if int(option_selected) == MENU_OPTIONS['1']['value']:
        print(MENU_OPTIONS['1']['log_pattern'].format(h=config.HOST, p=config.PORT))
        tcp_loop(validate_user)
    elif int(option_selected) == MENU_OPTIONS['2']['value']:
        print(MENU_OPTIONS['2']['title'])
        name = input(MENU_OPTIONS['2']['items']['name'])
        last_name = input(MENU_OPTIONS['2']['items']['last_name'])
        input(MENU_OPTIONS['2']['items']['ready'])
        print(MENU_OPTIONS['2']['log_pattern'].format(h=config.HOST, p=config.PORT))
        kwargs = {
            'name': name,
            'last_name': last_name,
        }
        tcp_loop(function=add_user, **kwargs)
    elif int(option_selected) == MENU_OPTIONS['3']['value']:
        print(MENU_OPTIONS['3']['title'])
        confirmation = input(MENU_OPTIONS['3']['confirmation'])
        if str(confirmation).upper() == 'Y':
            try:
                migrations.insert_users()
                print(MENU_OPTIONS['3']['ready'])
            except CustomIntegrityError as e:
                print(e.msg)
        else:
            print(MENU_OPTIONS['3']['cancel'])
    elif int(option_selected) == MENU_OPTIONS['4']['value']:
        print(MENU_OPTIONS['4']['title'])
        confirmation = input(MENU_OPTIONS['4']['confirmation'])
        if str(confirmation).upper() == 'Y':
            migrations.reset_and_create_schemas()
            print(MENU_OPTIONS['4']['ready'])
        else:
            print(MENU_OPTIONS['4']['cancel'])
    print(config.SERVER_END_MSG)


# Main body
if __name__ == '__main__':
    main()
