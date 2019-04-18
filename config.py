
# SERVER SETTINGS

# host
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# responses
SERVER_SUCCESS_RESPONSE = b'OK'
SERVER_ERROR_RESPONSE = b'ERROR'

# logging
SERVER_START_MSG = '--app started-- \n To close the app press CTRL-C'
SERVER_END_MSG = '--app closed--'
LOG_PATTERN = '{h}:{p} - Received: {m} - user: {u}'


# CLIENT SETTINGS

# logging
CLIENT_ERROR_RESPONSE_PATTERN = 'Connection error. Is server running? message: {}'
