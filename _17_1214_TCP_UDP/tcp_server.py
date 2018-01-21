import socket
from threading import Thread
import time


def new_sock(socket, addr):
    print(f'new connection {addr}')
    socket.send("welcome!".encode())

    while True:
        s = socket.recv(1024)
        time.sleep(1)
        if not s or s.decode() == 'exit':
            break
        socket.send("hello  ".encode() + s)
        print(addr, s.decode())

    socket.close()
    print(f'connection close {addr}')


def tcp_server():
    s = socket.socket()
    print("bind 127.0.0.1")
    s.bind(("127.0.0.1", 9999))
    s.listen(5)
    print('listen')

    while True:
        sock, addr = s.accept()
        t = Thread(target=new_sock, args=(sock, addr))
        t.start()


if __name__ == '__main__':
    tcp_server()
