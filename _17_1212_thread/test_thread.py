import time, threading
from multiprocessing import Process

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    # for n in range(5):
    #     print('thread %s >>> %s' % (threading.current_thread().name, n))
    #     time.sleep(1)
    n = 0
    for i in range(60000000):
        n += i
    print('thread %s ended.' % threading.current_thread().name)


def test_thread():
    print('thread %s is running...' % threading.current_thread().name)
    t1 = threading.Thread(target=loop, name='LoopThread')
    t2 = threading.Thread(target=loop, name='LoopThread')
    p = Process(target=loop,name='loopthread')
    t1.start()
    t2.start()
    p.start()
    t1.join()
    t2.join()
    p.join()
    print('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    test_thread()
