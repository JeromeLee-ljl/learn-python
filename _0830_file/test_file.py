import os


def find_file(key, path='.'):
    _find_file(key, path)


def _find_file(key, path, rel_path=''):
    abs_path = os.path.join(path, rel_path)
    if os.path.isfile(abs_path) and key in os.path.split(abs_path)[1]:
        print(rel_path)
        return

    if not os.path.isdir(abs_path): return

    for p in os.listdir(abs_path):
        _find_file(key, path, os.path.join(rel_path, p))


if __name__ == '__main__':
    find_file('tes', '../')
