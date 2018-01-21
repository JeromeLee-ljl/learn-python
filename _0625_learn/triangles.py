def triangles():
    l = [1]
    while True:
        yield l
        # temp = list(l)
        # i = 1
        # while i < len(temp):
        #     l[i] = temp[i-1] + temp[i]
        #     i = i+1

        # l = [l[i - 1] + l[i] for i in range(1, len(l))]
        # l.insert(0, 1)
        # l.append(1)

        l = [1] + [l[i - 1] + l[i] for i in range(1, len(l))] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
