def test_counter():
    from collections import Counter
    c = Counter()
    for ch in 'programming':
        c[ch] += 1
    print(c)


if __name__ == '__main__':
    test_counter()

