def test_base64():
    import base64
    jpg = open('./1.png', 'rb')
    byte = jpg.read()
    s = base64.b64encode(byte)
    print(s)
    print(base64.b64decode(b'YWJjZA=='))


if __name__ == '__main__':
    test_base64()
    b = bytes([1,2])
    print(b)
    print(type(b))
