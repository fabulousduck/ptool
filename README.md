# PTOOL

Ptool is a small set of functions that make it easier to get information about sockets, pids, and the network you are on. It offers simple queries into combinations of information regarding sockets, processes, and the network.

## Installing

Installing can be done by pasting the following commands into your terminal. (these might be slightly different if you're on windows).
This requires you to have git installed before you get started

```bash
$ git clone git@github.com:fabulousduck/ptool.git
$ cd ptool
$ chmod +x install.sh
$ ./install.sh
```

To test if the install was successful, you can try the following command after the installer is finished.

```bash
$ ptool -h
```

The following response should print to the screen.

```bash
usage: ptool [-h] [-a] [-p] [-pf [FINDPORT]] [-pk] [-n] [-nf]

better prockiller

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             print all available data
  -p, --ports           prints all ports and whats running on them
  -pf [FINDPORT], --findPort [FINDPORT]
                        finds a proc with a given port or description
  -pk, --portkill       kill the proc using a certail port
  -n, --network         prints all items on the network
  -nf, --networkfind    get info about a local network host given an ip
```