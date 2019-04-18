
import socket
import orm
import config

try:
    print(config.SERVER_START_MSG)
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
                    try:
                        user = orm.get_user_by_card_id(card_id=data)
                        if user:
                            conn.sendall(config.SERVER_SUCCESS_RESPONSE)
                        else:
                            conn.sendall(config.SERVER_ERROR_RESPONSE)
                        print(config.LOG_PATTERN.format(h=addr, m=data, u=user))
                    except Exception:
                        conn.sendall(config.SERVER_ERROR_RESPONSE)
except KeyboardInterrupt:
    print(config.SERVER_END_MSG)
