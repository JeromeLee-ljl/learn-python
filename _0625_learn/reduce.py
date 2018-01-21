from functools import reduce


# 1 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    # return name.lower().capitalize()
    return name[:1].upper() + name[1:].lower()


# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# 2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 4 * 2 * 1 =', prod([3, 4, 2, 1]))


# 3 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(char2num, s))

    ss = s.split('.')

    return str2int(ss[0]) + str2int(ss[1]) / pow(10, len(ss[1]))


print('str2float(\'123.456\') =', str2float('123.99999'))


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# -*- coding: utf-8 -*-

def is_palindrome(n):
    a = str(n)

    b = a[::-1]

    return a == b


# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))


def primes():
    def getnum():
        l = 2
        while True:
            yield l
            l = l + 1

    def is_not_multiple(n):
        return lambda x: x % n > 0

    numlist = getnum()
    while True:
        n = next(numlist)
        yield n

        numlist = filter(is_not_multiple(n), numlist)


# # 打印1000以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# 装饰器
import functools

def log(text="call"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(text, func.__name__)
            return func(*args, **kwargs)

        print("add decorator to", func.__name__)
        return wrapper

    return decorator


@log()
def test():
    print("test func")

# test()
# end 装饰器

import sys

def test():
    args = sys.argv
    print(args)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
