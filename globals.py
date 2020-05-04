# Writer: Gal Harari
# Date: 28/11/2019
import socket

# --------------------------------------- ports and ip -----------------------------------
SERVER_PORT = 1234
ATTACKER_SERVER_PORT = 1234
VICTIM_SERVER_PORT = 1237
LOOPBACK_IP = "127.0.0.1"
SERVER_IP = "139.162.184.23"

# ---------------------------------------- commands --------------------------------------
LEFT_CMD = 'L'
RIGHT_CMD = 'R'
FORWARD_CMD = 'F'
BACK_CMD = 'B'
STOP_CMD = ' '
OK_SIGNAL = 'OK'

# ---------------------------------------- others ----------------------------------------
BUF_SIZE = 1024
SMALL_BUF_SIZE = 10
CMD_SIZE = 1
OK_SIZE = len(OK_SIGNAL)
SPLIT_CHAR = "#"
# it comes as 'VI'\'AT' + <tool_id>
VICTIM_ID = 'VI'
ATTACKER_ID = 'AT'

ID_LEN = len(ATTACKER_ID)


# ---------------------------------------- functions -------------------------------------
def recvall(sock, size):
    received_chunks = []
    buf_size = 4096
    remaining = size
    while remaining > 0:
        received = sock.recv(min(remaining, buf_size))
        if not received:
            raise Exception('unexpected EOF')
        received_chunks.append(received)
        remaining -= len(received)
    return b''.join(received_chunks)


def send_long_msg(s: socket.socket, msg):
    """
    gets unknown length, long message out of socket. gets in byte format
    :param s:
    :return:the message from the socket
    """
    print("Waiting for an OK to start")
    while s.recv(OK_SIZE).decode() == '':
        pass

    print(f"Sending the message length {len(msg)}")
    # first send the length of the message we are going to send
    s.send(str(len(msg)).encode())

    print("Waiting for an OK...")
    # wait for an "OK"
    while s.recv(OK_SIZE).decode() == '':
        pass

    print("Sending the message")
    # then send the message
    s.sendall(msg)

    print("Receiving an OK")
    # get an ok
    return s.recv(OK_SIZE).decode()


def get_long_msg(s: socket.socket):
    """
    gets unknown length, long message out of socket. gets in byte format
    :param s:
    :return:the message from the socket in byte format
    """
    print("Sending OK to start")
    s.send(OK_SIGNAL.encode())

    print("Receiving length...")
    # first get the length of the message we are going to send
    length = int((s.recv(SMALL_BUF_SIZE)).decode())
    print("length: ", length)

    print("Sending OK")
    # send an "OK"
    s.send(OK_SIGNAL.encode())

    print("Receiving the message...")
    # then get the message
    msg = recvall(s, length)

    print(f"Got message in length {len(msg)}.Sending OK")
    # send ok
    s.send(OK_SIGNAL.encode())
    return msg
