class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self.birth


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


if __name__ == '__main__':
    s = Student()
    s.birth = 2000

    foo('0')
    print('sd')
