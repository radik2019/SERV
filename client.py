

import threading
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.117', 8080))


def snd():

    print('snd    ')
    while True:
        sock.send(bytes('>   ' + input(), encoding='utf-8'))


def rcv():
    print('rcv    ')
    while True:
        data = sock.recv(1024)
        print(data.decode(encoding="utf-8"))


t1 = threading.Thread(target=snd)
t2 = threading.Thread(target=rcv)
t1.start()
t2.start()
t1.join()
t2.join()