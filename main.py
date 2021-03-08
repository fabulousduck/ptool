import argparse
import socket
import sys
import os

def main():
    parser = argparse.ArgumentParser(prog='ptool', description='better prockiller')
    parser.add_argument('-a', '--all', action='store_true', help='print all available data')
    parser.add_argument('-p', '--ports', action='store_true', help='prints all ports and whats running on them')
    parser.add_argument('-pf', '--findPort', nargs='?',  help='finds a proc with a given port or description')
    parser.add_argument('-pk', '--portkill', action='store_true', help='kill the proc using a certail port')
    parser.add_argument('-n', '--network', action='store_true', help='prints all items on the network')
    parser.add_argument('-nf', '--networkfind', action='store_true', help='get info about a local network host given an ip')
    
    args = parser.parse_args()
    
    if not any(vars(args).values()):
        parser.print_help()
        sys.exit(1)

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
    elif args.findPort:
        findPort(False, args.findPort)

def all():
    return

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def getPidList(OS): #TODO: use OS var for windows
    ls = []
    cmd = 'ps -ef'
    for x in os.popen(cmd):
        if "UID" not in x:
            n = list(filter(None,x.split(' ')))
            ls.append((n[1], n[7].rstrip('\n')))
    return ls

#format the netstat output and format to port list
def handleNetstat(isWindowsWSL):
    ls = []
    #workaround for WSL where base netstat doesnt work
    baseCmd = 'netstat.exe' if isWindowsWSL else 'netstat'
    netCmd = f'{baseCmd} -ano -p tcp'
    for x in os.popen(netCmd):
        n = list(filter(None,x.split(' ')))
        if n[0] == 'TCP': 
            port = int(n[2].split(':')[1])
            pid = int(n[4])
            ls.append((port,pid, 'NO DESCRIPTION'))
    
    ls.sort(key=lambda tup: tup[0])

    return ls

def isWSL():
    if sys.platform == 'linux' or platform == 'linux32':
        #make sure we're on actual linux and not WSL
        fp = open('/proc/version')
        if 'Microsoft' in fp.read():
            return True
    return False

"""
find a specific port with some proc running it
returns (port, pid)
if it finds nothing by that port, it returns (-1,-1)
"""
def findPort(ret, arg):
    portPidList = handleNetstat(isWSL())
    pidDescriptionList = getPidList("WSL")
    printableList = []
    

    for idx, (pid, desc) in enumerate(pidDescriptionList):
        for i, item in enumerate(portPidList):
            if pid == item[0]:
                portPidList[i] = (item[0], item[1], desc)
                del pidDescriptionList[idx]
                break
    for pid, desc in pidDescriptionList:
        portPidList.append((-1, pid, desc))

    if isInt(arg):        
        for port, pid, desc in portPidList:
            if int(port) == int(arg):
                printableList.append((port,pid,desc))
    else:
        for port, pid, desc in portPidList:
            if arg in desc:
                printableList.append((port, pid, desc))

    if len(printableList) < 1:
        print(f'No result for {arg}')
        return (-1,-1)

    for port, pid, desc in printableList:
        port = 'NO PORT' if port == -1 else port
        print(f'PORT: {port}, PID: {pid}, DESC: {desc}')
    return printableList

#kill a process with a given port
def portkill():
    return


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
                    print(f'\tport: {x[0]}, pid: {x[1]}')
                fp.close()
        else:
            ports = handleNetstatPortList(False)
    elif sys.platform == 'darwin':
        print('OSX is currently not supported')
        return
    elif sys.platform == 'win32':
        print('Windows is currently not supported')
        return

    return

def netfind(ret):
    return

def netscan(ret):
    return


if __name__ == "__main__":
    main()
