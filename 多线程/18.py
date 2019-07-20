import multiprocessing
from time import ctime,sleep

class clockprocess(multiprocessing.Process):
    '''
    两个函数比较重要
    1.init构造函数
    2.run函数
    '''
    def __init__(self,intt):
        super().__init__()
        self.intt = intt

    def run(self):
        while True:
            print("当前时间%s" % ctime())
            sleep(self.intt)


if __name__ == '__main__':
    p = clockprocess(3)
    p.start()
    p.join()