import main
import socket

def bootFakeSocket():
    testSockHost = '127.0.0.1'
    testSockPort = 3002
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((testSockHost, testSockPort))
    except socket.error as msg:
        print('socket bind failed, aborting ports test')
        return
    s.listen(10)

def test_ports():
    s = bootFakeSocket()    
    main.ports(False)
    s.close()
    
    return

if __name__ == '__main__':
    test_ports()