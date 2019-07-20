import time
import threading
def loca1():
    print("set loca1 ",time.ctime())
    time.sleep(4)
    print("end loca1",time.ctime())

def loca2():
    print("set loca2 ",time.ctime())
    time.sleep(1)
    print("end loca2",time.ctime())

def loca3():
    print("set loca3 ",time.ctime())
    time.sleep(6)
    print("end loca3",time.ctime())

def main():
    print("这是main函数执行开始时间",time.ctime())

    t1 = threading.Thread(target=loca1,args=())
    #给每个线程设置一个名字，不设置名字为Thread-1
    t1.setName('thr1')
    t1.start()

    t2 = threading.Thread(target=loca2,args=())
    t2.setName('thr2')
    t2.start()

    t3 =threading.Thread(target=loca3,args=())
    t3.setName('thr3')
    t3.start()

    time.sleep(3)
    #得到当前正在执行的loca1和loca3还有一个主线程
    for thr in threading.enumerate():
        #getName得到线程的名字
        print("正在执行的县城名字{0}".format(thr.getName()))

    print("正在执行的线程数量{0}".format(threading.activeCount()))

    print("main结束时间",time.ctime())

if __name__ == '__main__':

    main()
    #在threading里面主线程结束后子线程也不会终止