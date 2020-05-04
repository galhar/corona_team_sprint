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


