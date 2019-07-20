import time
import threading
#类必须继承自threading.Thread
class mythread(threading.Thread):
    def __init__(self,arg):
        super(mythread,self).__init__()
        self.arg = arg
    #必须重写run函数，run函数代表的是真正执行的功能
    def run(self):
        time.sleep(2)
        print("dayinchu  {0}".format(self.arg))

for i in range(5):
    t = mythread(i)
    t.start()
    t.join()

print("===================")