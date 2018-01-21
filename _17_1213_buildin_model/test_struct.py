def test():
    import struct
    print(struct.pack('>I', 10240099))


def test_hmac():
    import hmac
    message = b'Hello, world!'
    key = b'secret'
    h = hmac.new(key, message, digestmod='MD5')
    # 如果消息很长，可以多次调用h.update(msg)
    print(h.hexdigest())


if __name__ == '__main__':
    test()
    test_hmac()
    import datetime
    print(datetime.datetime.strptime("Tue Oct 11 02:27:26 +0000 2016",'%a %b %d %H:%M:%S %z %Y'))
