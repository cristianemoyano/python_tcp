
import config
import menu
import actions


def main():
    print(config.SERVER_START_MSG)
    print(menu.generate_option_labels())
    option_selected = input(menu.MENU_START_MSG)
    if int(option_selected) == menu.MENU_OPTIONS['1']['value']:
        # ---- Validate users ------
        actions.validate_user_action()
    elif int(option_selected) == menu.MENU_OPTIONS['2']['value']:
        # ---- Add user ------
        actions.add_user_action()
    elif int(option_selected) == menu.MENU_OPTIONS['3']['value']:
        # ---- Run migrations ------
        actions.run_migrations_action()
    elif int(option_selected) == menu.MENU_OPTIONS['4']['value']:
        # ---- Reset and create schemas ------
        actions.reset_and_create_schemas_action()

    # ---- Exit ------
    print(config.SERVER_END_MSG)


# Main body
if __name__ == '__main__':
    main()
