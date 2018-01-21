import socket


def test():
    s = socket.socket()
    s.connect(('127.0.0.1', 9999))

    # 欢迎消息
    print(s.recv(1024).decode())

    while True:
        i = input("send>> ")

        s.send(i.encode())
        if i == 'exit':
            break
        re = s.recv(1024).decode()

        print(f'recv<< {re}')

    s.close()


if __name__ == '__main__':
    test()
