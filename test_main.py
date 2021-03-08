import main
import socket

def bootTestSocket():
    testSockHost = '127.0.0.1'
    testSockPort = 3002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((testSockHost, testSockPort))
    except socket.error as msg:
        print('socket bind failed, aborting ports test')
        sys.exit()
    s.listen(10)
    return s

def test_portfind():
    s = bootTestSocket()
    res = main.findPort(True, 3002)
    assert res != (-1,-1), "port 3002 not running"
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
    test_ports()
    test_portfind()