import threading
sum = 0
num = 100000
lock = threading.Lock()
def add():
    global sum,num
    for i in range(1,num):
        #上锁，申请锁
        lock.acquire()
        sum += 1
        #释放锁，只有释放了锁别的线程才能用共享资源
        lock.release()

def jian():
    global sum,num
    for i in range(1,num):
        lock.acquire()
        sum -= 1
        lock.release()

if __name__ == '__main__':
    print("sum 开始为{0}".format(sum))

    t1 = threading.Thread(target=add,args=())
    t2 = threading.Thread(target=jian,args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(sum)