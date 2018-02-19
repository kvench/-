#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
while True:
    a = input()
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(a.encode('utf-8'))
    data = sock.recv(1024)
    sock.close()
    print(data.decode('utf-8'))


