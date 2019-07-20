import threading
from time import sleep,ctime

loop = [2,2]

class ter():
    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        '''
        naloop 函数loop的名称
        nsec 系统休眠时间


        '''
        print("-----",nloop,ctime())
        sleep(nsec)
        print("======",nloop,ctime())

def main():
    print("main yunxing shijian ==",ctime())
    # 类实例化
    t = ter("Loop")
    #传入名称是为了区分子线程
    t1 = threading.Thread(target=t.loop,args=("dada1",2))
    # 更工业化一点
    t2 = threading.Thread(target=ter('Loop').loop,args=("dada",2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("程序结尾了",ctime())

if __name__ == '__main__':
    main()