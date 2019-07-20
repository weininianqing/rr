import time
import threading

def fun():
    print("fun函数开头")
    time.sleep(2)
    print("睡醒了的fun")

print("程序的入口")
t = threading.Thread(target=fun,args=())
t.start()
time.sleep(1)
print("程序的结束口")#执行这句话主线程就结束了，但是子线程却还在执行