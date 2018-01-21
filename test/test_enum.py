from enum import Enum


if __name__ == '__main__':
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    print(Month)
    print(Month.__members__)
    print(Month.__members__.items())
    for name,v in Month.__members__.items():
        print(name,v)
