class Person(object):
    def __init__(self):
        self._name = "s"

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name


def showname(self):
    print(self._name)


Person.showname = showname
a = Person()
a.showname()




class Chain(object):

    name = "asf"
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    #只需添加如下的 __call__() 函数即可
    def __call__(self,path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users('michael').repos)

print(Chain.__dict__)