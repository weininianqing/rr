import threading
sum = 0
num = 100000

def add():
    global sum,num
    for i in range(1,num):
        sum += 1

def jian():
    global sum,num
    for i in range(1,num):
        sum -= 1

if __name__ == '__main__':
    print("sum 开始为{0}".format(sum))

    t1 = threading.Thread(target=add,args=())
    t2 = threading.Thread(target=jian,args=())
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print(sum)
# 因为 自加1和自减1的执行过程不是一下完成，出现这样的问题是在加1过程中，还没算出来就应经被减1的拿走了运算去了
#乱套了就