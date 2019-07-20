import time
import threading


lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
    print("申请锁lock1..")
    lock1.acquire()
    print("睡两秒")
    time.sleep(2)

    print("申请锁lock2，等待中...")
    lock2.acquire()
    print("释放锁lock2")
    lock2.release()
    print("释放锁lock1")
    lock1.release()


def fun2():
    print("申请锁lock2..")
    lock2.acquire()
    print("睡四秒")
    time.sleep(4)

    print("申请锁lock1，等待中")
    lock2.acquire()
    print("释放锁lock1")
    lock2.release()
    print("释放锁lock2")
    lock1.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=fun1,args=())
    t2 = threading.Thread(target=fun2,args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序完蛋了")