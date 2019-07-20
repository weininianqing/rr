import multiprocessing
from time import ctime,sleep
import os

def info(title):
    print(title)
    #这里就是当前进程的名字
    print("当前进程名字",__name__)
    #父亲进程的id
    print("父进程id",os.getppid())
    #自己当前进程的id
    print("自己进程id",os.getpid())

def f(name):
    info('f 调用')
    print("hello",name)

if __name__ == '__main__':
    info("主进程开始")
    p = multiprocessing.Process(target=f,args=("宝宝",))
    p.start()
    p.join()