def hannuo(num, a, b, c):
    if num == 1:
        print(a, "-->", c)
        return
    hannuo(num - 1, a, c, b)
    hannuo(1, a, b, c)
    hannuo(num - 1, b, a, c)


hannuo(3, 'A', 'B', 'C')