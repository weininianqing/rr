import multiprocessing
from time import ctime,sleep

def clock(inte):
    while True:
        print("当前时间%s"%ctime())
        sleep(inte)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock,args=(3,))
    p.start()
    p.join()