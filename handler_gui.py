# Writer: Gal Harari
# Date: 04/05/2020
import socket
import time
from globals import *
import msvcrt

key_to_cmd = {
    b'a': LEFT_CMD,
    b'w': FORWARD_CMD,
    b'd': RIGHT_CMD,
    b's': BACK_CMD,
    b' ': STOP_CMD
}

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
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            print(key_stroke)
            cmd = key_to_cmd.get(key_stroke, None)
            if cmd:
                s.send(cmd.encode())
