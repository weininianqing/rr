import time
import threading
import queue

class pro(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize()<1000:
                for i in range(100):
                    count += 1
                    msg = '生产产品'+str(count)
                    #想queue里面添加
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class con(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(3):
                    #提取出queue一个东西
                    msg = self.name+'消费了'+queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))

    for i in range(2):
        p = pro()
        p.start()
    for i in range(5):
        c = con()
        c.start()
