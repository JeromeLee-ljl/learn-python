# 在 Python 中，内层函数对外层作用域中的变量仅有只读访问权限！
# 而 nonlocal 可以使我们自由地操作外层作用域中的变量！


def createCounter():
    count = [0]

    def counter():
        nonlocal count
        count = count + [9]
        return count[0]

    return counter


if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
