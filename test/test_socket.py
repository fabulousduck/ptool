import socket
import sys
testSockHost = '127.0.0.1'
testSockPort = 3002
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((testSockHost, testSockPort))
except socket.error as msg:
    print(msg)
    print('socket bind failed, aborting ports test')
    sys.exit()
s.listen(1)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    conn.sendall(data)
