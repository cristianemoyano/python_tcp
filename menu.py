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
        'label': 'Add user',
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

MENU_TITLE = "Menu: "


def generate_option_labels():
    j = ' \n '
    d = '.'
    s = ' '
    options = MENU_TITLE + j
    for key, opt in MENU_OPTIONS.items():
        options += key + d + s + opt.get('label') + j
    return options
