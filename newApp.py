
import socket
import threading


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(("192.168.1.117", 8080))
soc.listen(10)
conn, addr = soc.accept()

ip, port = addr
print(ip, port)


def send_message():
    print("send message ...   ")
    while True:
        conn.send(bytes("pc:   " + input("io:  "), encoding="utf-8"))


def receve_message():
    print("receve message ...  ")
    while True:
        data = conn.recv(1024)
        if not data:
            soc.close()

        print(data.decode(encoding="utf-8"))


t1 = threading.Thread(target=send_message)
t2 = threading.Thread(target=receve_message)

t1.start()
t2.start()
t1.join()
t2.join()



