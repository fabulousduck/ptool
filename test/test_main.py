import subprocess
import signal
import socket
import sys
import os
sys.path.append("..")
from main import findPort, ports

def test_portfind():
    res = findPort(True, 3002)
    assert res != (-1,-1), "portfind FAIL"
    print("portfind OK")
    return

def test_ports():
    ret = ports(True)
    print("portlist OK")
    return

if __name__ == '__main__':
    socketPid = subprocess.Popen([sys.executable, 'test_socket.py'])
    test_ports()
    test_portfind()
    print(socketPid)
    os.kill(socketPid.pid, signal.SIGTERM)