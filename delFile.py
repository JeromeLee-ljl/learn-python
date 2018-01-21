import os

import shutil
import os
from os.path import join, getsize


def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size


buildSize = 0


def scandir(startdir, target):
    global buildSize
    os.chdir(startdir)
    for obj in os.listdir(os.curdir):
        if obj == target:
            print(os.getcwd() + os.sep + obj)
            try:
                # os.remove(obj)
                buildSize = getdirsize(obj) + buildSize
                shutil.rmtree(obj)
            except IOError:
                print("except")
        if os.path.isdir(obj):
            scandir(obj, target)
            os.chdir(os.pardir)  # !!!


scandir("C:/Users/Steven/OneDrive/AndroidStudioProjects", "build")
print(buildSize/1024/1024,"MB")
