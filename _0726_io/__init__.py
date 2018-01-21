# 文件读取
# def readfile():
#     with open("C:\\Users\\Steven\\OneDrive\\PycharmProjects\\learn\\_0726_io\\__init__.py", "r", encoding='utf-8') as f:
#         print(f.read(25))
#
#
# readfile()
#
# import os
#
# print(os.name)
# print(os.environ)
# print(os.environ.get('path'))
# print(os.uname()) windows 不支持

import os
import re


def find_file_like(key):

    root = os.path.abspath(".")
    print("%s\n\t find file like:'%s'" % (root, key))
    _find_file_like(root, "", key)


def _find_file_like(root, rel_path, key):
    abspath = os.path.join(root, rel_path)
    for x in os.listdir(abspath):
        f = os.path.join(abspath, x)
        _rel_path = os.path.join(rel_path, x)
        if os.path.isdir(f):
            _find_file_like(root, _rel_path, key)
        elif re.search(key, x):
            print("...", _rel_path)


if __name__ == "__main__":
    find_file_like("init")

import pickle

