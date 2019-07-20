import time
import threading

def loc1(a):
    print("刚开始执行时间loc1",time.ctime())
    print("我是参数",a)
    time.sleep(4)
    print("休息之后的时间loc1",time.ctime())

def loc2(b,c):
    print("刚开始执行时间loc2",time.ctime())
    print(b,c,"参数")
    time.sleep(2)
    print("休息之后的时间loc2",time.ctime())

def main():
    print("程序运行时间",time.ctime())
    t1 = threading.Thread(target=loc1,args=("woai",))
    t1.start()
    t2 = threading.Thread(target = loc2,args=("灰灰","佳佳"))
    t2.start()
    t1.join()
    t2.join()

    print("程序完成时间",time.ctime())

if __name__ == '__main__':
    main()