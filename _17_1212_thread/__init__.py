from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print(f'Run child p {name} id {os.getpid()}')


def test_Process():
    print(f'Parent pid {os.getpid()}.')
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    print('start')
    p.join()
    print('Child process end.')


from multiprocessing import Pool
import time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()), flush=True)
    start = time.time()
    time.sleep(random.random() * 2)

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)), flush=True)


class A(object):
    pass


def test_Pool():
    print('Parent process %s.' % os.getpid())
    p = Pool()
    print(type(Pool))
    print(type(A))

    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


def test_subprosess():
    import subprocess
    print('$ nslookup')
    p = subprocess.Popen(['python','../_0830_file/__init__.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'hello')
    print(output.decode())
    print('Exit code:', p.returncode)


from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def test_Queue():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    # test_Process()
    # print("\n")
    # test_Pool()
    # print("\n")
    # test_subprosess()
    print("\n")
    test_Queue()
