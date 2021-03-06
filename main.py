import argparse
import socket
import sys
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

#format the netstat output and format to port list
def handleNetstat(isWindowsWSL):
    ls = []
    #workaround for WSL where base netstat doesnt work
    baseCmd = 'netstat.exe' if isWindowsWSL else 'netstat'
    netCmd = f'{baseCmd} -ano -p tcp'
    for x in os.popen(netCmd):
        n = list(filter(None,x.split(' ')))
        if n[0] == 'TCP': 
            port = n[1].split(':')[1]
            pid = n[4]
            ls.append((port,pid))

    return ls

#list all open ports and the pids for the procs using them
def ports(ret):

    if sys.platform == 'linux' or platform == 'linux32':
        #make sure we're on actual linux and not WSL
        fp = open('/proc/version')
        if 'Microsoft' in fp.read():
            procPortList = handleNetstat(True)
            if ret:
                fp.close()
                return procPortList
            else:
                for x in procPortList:
                    print(f'port: {x[0]}, pid: {x[1]}')
                fp.close()
        else:
            ports = handleNetstatPortList(False)
    elif sys.platform == 'darwin':
        print('OSX is currently not supported')
        return
    elif sys.platform == 'win32':
        print('Windows is currently not supported')
        return
    
    # procList  = [(int(port), command) for port,command in [x.rstrip('\n').split(' ', 1) for x in os.popen('ps h -eo pid:1,command')]]
    # portList = [x for x in os.popen('ss -tulpn')]

    return

def netfind(ret):
    return

def netscan(ret):
    return

    
if __name__ == "__main__":
    main()
