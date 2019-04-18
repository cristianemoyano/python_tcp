import socket
import config

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((config.HOST, config.PORT))
        # Test with correct user
        s.sendall(b'ASF1235')
        data = s.recv(1024)
        print('Received from server: ', repr(data))

        # Test with wrong user
        s.sendall(b'WRONG_ID')
        data = s.recv(1024)
        print('Received from server: ', repr(data))
except socket.error as e:
    print(config.CLIENT_ERROR_RESPONSE_PATTERN.format(e))
