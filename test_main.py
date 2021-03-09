import main
import socket

testSocketUp = False
testSockHost = '127.0.0.1'
testSockPort = 3002

def bootTestSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((testSockHost, testSockPort))
    except socket.error as msg:
        print('socket bind failed, aborting ports test')
        sys.exit()
    s.listen(1)
    conn, addr = s.accept()
    while testSocketUp:
        data = conn.recv(1024)
        conn.sendall(data)
    return s

def test_portfind():
    s = bootTestSocket()
    res = main.findPort(True, 3002)
    assert res != (-1,-1), "portfind FAIL"
    s.close()
    print("portfind OK")
    return

def test_ports():
    s = bootTestSocket()    
    ret = main.ports(True)
    s.close()
    print("portlist OK")
    return



if __name__ == '__main__':
    # test_ports()
    # test_portfind()
    testSocketUp = True
    s = bootTestSocket()
    print(conn, addr)