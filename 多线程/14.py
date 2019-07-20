import time
import threading

def func():
    print("运行开始了...")
    time.sleep(4)
    print("I am done.............")

if __name__ == '__main__':
    #6秒以后启动函数func
    t = threading.Timer(6,func)
    t.start()

    i = 0
    while True:
        print("{0}==============".format(i))
        time.sleep(3)
        i += 1