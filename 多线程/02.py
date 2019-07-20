import time
import _thread as thread

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
    #启动多线程的意思就是用多线程去执行某个函数
    #启动多线程的函数star_new_thread
    #参数两个，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空使用空元组
    #注意如果函数参数只有一个，参数后面加一个逗号
    thread.start_new_thread(loc1,("凡是拿",))
    thread.start_new_thread(loc2,("woshi","dana"))
    print("程序完成时间",time.ctime())


if __name__ == '__main__':
    main()
    # 这里的while死循环目的就是不让程序结束，等待上面的时间
    while True:
        time.sleep(1)