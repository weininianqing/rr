import time
import threading


lock1 = threading.Lock()
lock2 = threading.Lock()

def fun1():
    print("申请锁lock1..")
    lock1.acquire(timeout=4)
    print("申请到了lock1")
    print("睡两秒")
    time.sleep(2)

    print("申请锁lock2，等待中...")
    rst = lock2.acquire(timeout=2)
    if rst:
        print("申请到了lock2 开心")
        lock2.release()
        print("释放lock2")
    else:
        print("没有申请到锁lock2")


    print("释放锁lock1")
    lock1.release()


def fun2():
    print("申请锁lock2..")
    lock2.acquire(timeout=2)
    print("申请到了锁lock2")
    print("睡四秒")
    time.sleep(4)

    print("申请锁lock1，等待中")
    rst = lock1.acquire(timeout=2)
    if rst:
        print("申请到了lock1 开心")
        lock1.release()
        print("释放锁lock1")
    else:
        print("没有申请到lock1")

    lock2.release()
    print("释放锁lock2")


if __name__ == '__main__':
    t1 = threading.Thread(target=fun1,args=())
    t2 = threading.Thread(target=fun2,args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序完结束了")