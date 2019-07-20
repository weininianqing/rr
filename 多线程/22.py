import multiprocessing
from time import ctime,sleep

def con(input_q):
    print("消费开始时间",ctime())
    while True:
        #处理项
        item = input_q.get()
        if item is None:
            break
        print("消费了",item)
        input_q.task_done()#发送信号通知任务完成
    print("消费结束时间",ctime())

def pro(s,out_q):
    print("生产时间",ctime())
    for i in s:
        out_q.put(i)
        print("生产了",i)
    print("生产结束时间",ctime())

#建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    con_p1=multiprocessing.Process(target=con,args=(q,))
    con_p2=multiprocessing.Process(target=con,args=(q,))
    con_p2.start()
    con_p1.start()

    #生产多个项，sequence代表要发送给消费者的项序列
    #在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4,5]
    #调用pro函数
    pro(sequence,q)
    #等待所有项被拿出来，主进程在结束
    q.put(None)
    q.put(None)

    con_p1.join()
    con_p2.join()