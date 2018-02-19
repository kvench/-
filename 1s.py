#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
while True:
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print ('connected:', addr)


    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    conn.send(data.upper().encode('utf-8'))

    conn.close()
