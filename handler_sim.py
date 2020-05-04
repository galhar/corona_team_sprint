# Writer: Gal Harari
# Date: 04/05/2020
import socket
import time
from globals import *

HOST = SERVER_IP  # The server's hostname or IP address
PORT = ATTACKER_SERVER_PORT  # The port used by the server


def connect_protocol(s):
    s.send(ATTACKER_ID.encode())

    # get an OK signal
    inp = ''
    inp = s.recv(OK_SIZE).decode()

    print(f'Got from the server: {inp}')
    return s


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s = connect_protocol(s)
    while True:
        s.send('F'.encode())
        time.sleep(2)
        s.send('B'.encode())
        time.sleep(2)
