import argparse
import sys
import socket
import os

def main():


    parser = argparse.ArgumentParser(prog='ptool', description='better prockiller')
    parser.add_argument('-a', '--all', action='store_true', help='print all available data')
    parser.add_argument('-p', '--ports', action='store_true', help='prints all ports and whats running on them')
    parser.add_argument('-pf', '--portfind', action='store_true', help='finds a proc with a given port')
    parser.add_argument('-pk', '--portkill', action='store_true', help='kill the proc using a certail port')
    parser.add_argument('-n', '--network', action='store_true', help='prints all items on the network')
    parser.add_argument('-nf', '--networkfind', action='store_true', help='get info about a local network host given an ip')

    args = parser.parse_args()
    
    if args.all:
        all()
    elif args.ports:
        ports(False)
    elif args.network:
        netscan(False)
    elif args.networkfind:
        netfind(False)
    elif args.portkill:
        portkill(False)
    elif args.portfind:
        portfind(False)

def all():
    return

#find a specific port with some proc running it
def portfind(ret): 
    return

#kill a process with a given port
def portkill():
    return

#list all open ports and the pids for the procs using them
def ports(ret):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.01'))

    procList  = [(int(port), command) for port,command in [x.rstrip('\n').split(' ', 1) for x in os.popen('ps h -eo pid:1,command')]]
    portList = [x for x in os.popen('ss -tulpn')]

    if len(portList) == 0:
        print('No ports active.')
        exit()

    print(portList)

    return

def netfind(ret):
    return

def netscan(ret):
    return

    
if __name__ == "__main__":
    main()
